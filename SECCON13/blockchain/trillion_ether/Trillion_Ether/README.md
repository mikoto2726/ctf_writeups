# **TrillionEther CTF 問題の解析とエクスプロイト検討**


### 自分の考えたシナリオ
- コントラクトの脆弱性を利用して、ウォレットの利用者になりすますことができる
- コントラクトの所有者になりすまして、コントラクトから他のウォレットに送金することで残高を0にすることができると考えました。
- しかし、コントラクトの所有者を変更する方法がわからなかったため、この方法は実現できませんでした。
- exploit3.pyが一番うまく行きそうでしたが逆にコントラクトの残高を増やしてしますことに...
- exploit3.py実行結果
```
> nc trillion-ether.seccon.games 31337
1 - launch new instance
2 - kill instance
3 - get flag (if isSolved() is true)
action? 1

== PoW ==
  sha256("80b733ed808a8c6e" + YOUR_INPUT) must start with 24 zeros in binary representation
  please run the following command to solve it:
    python3 <(curl -sSL https://minaminao.github.io/tools/solve-pow.py) 80b733ed808a8c6e 24

  YOUR_INPUT = 7052977

  sha256("80b733ed808a8c6e7052977") = 00000047e08fb8a32995e24b923bc2863fc9cfada4be229fa875f80e07062de2
  correct
== END POW ==
deploying your private blockchain...

your private blockchain has been deployed
it will automatically terminate in 10 minutes
here's some useful information
uuid:               84f69a5a-81c1-4e68-8d35-3a9979283d4c
rpc endpoint:       http://trillion-ether.seccon.games:8545/84f69a5a-81c1-4e68-8d35-3a9979283d4c
private key:        a1a96e9d885ce4dd7d3d7b36c159ebcb9aaa75c9b7c6aa705073efe0f1440f76
your address:       0x2889f2E4407D9Af92F889A549556dC67f1Ab8487
challenge contract: 0x59f476914F1Ff9186e3149E0cdC5F7d1885595Da
```
```
> python3 exploit3.py           
=== TrillionEther CTF Exploit Script ===

Enter the RPC endpoint URL:   http://trillion-ether.seccon.games:8545/84f69a5a-81c1-4e68-8d35-3a9979283d4c
Enter your private key (input hidden): a1a96e9d885ce4dd7d3d7b36c159ebcb9aaa75c9b7c6aa705073efe0f1440f76
Enter your Ethereum address: 0x2889f2E4407D9Af92F889A549556dC67f1Ab8487
Enter the challenge contract address: 0x59f476914F1Ff9186e3149E0cdC5F7d1885595Da
Connected to RPC endpoint.
Using account: 0x2889f2E4407D9Af92F889A549556dC67f1Ab8487
Contract instance created.

=== Starting Exploit ===

--- Step 1: Check Account Balance ---
Your account balance: 1 ETH

--- Step 2: Check Contract's Balance ---
Current contract balance: 1000000000000 ETH
Calculated deposit amount: 0.999 ETH

--- Step 3: Create a Wallet with Deposit ---

Creating wallet 'ExploitWallet' with 0.999 ether.
Transaction sent: 737ef19e36a2eb6cf981e6231a23c39b21ddb64f413793548ce441d437da9f6b
Transaction mined in block 3.
Wallet 'ExploitWallet' created successfully.

--- Wallet Balances ---
Wallet ID 0 balance: 0 ETH
-----------------------


--- Step 5: Withdrawing 0.999 ether from wallet ID 0 ---

Withdrawing 0.999 ether from wallet ID 0.
Transaction sent: dfd77247d4c5f5c561e286dafad8a23f529fc3934e3fdaaa290434c33e9cd778
Transaction mined in block 4.
Withdrawal from wallet ID 0 successful.

--- Wallet Balances ---
Wallet ID 0 balance: 0 ETH
-----------------------


--- Step 7: Checking if the contract is solved ---
Exploit failed. isSolved() is still False.

--- Final Contract Balance ---
Current contract balance: 1000000000000.999 ETH
Final contract balance: 1000000000000.999 ETH
```
### 以下はChatGPTと格闘した会話のまとめです
---

#### **問題の概要**
- **スマートコントラクト**:
  - TrillionEtherというスマートコントラクトが提供され、コントラクト内のETH残高をゼロにする必要がある。
  - コントラクトの構造上、`isSolved()` 関数が `True` を返すには、コントラクトのETH残高が完全にゼロになる必要がある。

- **現状**:
  1. コントラクトには以下のような関数が実装されている。
     - `createWallet`: 新しいウォレットを作成する。
     - `transfer`: ウォレット間での資金移動を行う。
     - `withdraw`: ウォレットから所有者がETHを引き出す。
     - `_newWallet`: 内部関数でウォレットのデータを設定。
  2. `createWallet` 関数にバグがあり、ウォレットの所有者が `0x0000000000000000000000000000000000000000` に設定されてしまう。
  3. 全ウォレットのバランスが0 ETHに設定され、実際にETHを引き出すことができない。

---

#### **スマートコントラクトのコード**
```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

contract TrillionEther {
    struct Wallet {
        bytes32 name;
        uint256 balance;
        address owner;
    }

    Wallet[] public wallets;

    constructor() payable {
        require(msg.value == 1_000_000_000_000 ether);
    }

    function isSolved() external view returns (bool) {
        return address(this).balance == 0;
    }

    function createWallet(bytes32 name) external payable {
        wallets.push(_newWallet(name, msg.value, msg.sender));
    }

    function transfer(uint256 fromWalletId, uint256 toWalletId, uint256 amount) external {
        require(wallets[fromWalletId].owner == msg.sender, "not owner");
        wallets[fromWalletId].balance -= amount;
        wallets[toWalletId].balance += amount;
    }

    function withdraw(uint256 walletId, uint256 amount) external {
        require(wallets[walletId].owner == msg.sender, "not owner");
        wallets[walletId].balance -= amount;
        payable(wallets[walletId].owner).transfer(amount);
    }

    function _newWallet(bytes32 name, uint256 balance, address owner) internal returns (Wallet storage wallet) {
        wallet = wallet;
        wallet.name = name;
        wallet.balance = balance;
        wallet.owner = owner;
    }
}
```

---

#### **実行結果の要約**
1. ウォレットの作成は成功するが、すべてのウォレットが以下の状態になる：
   - **名前**: 空
   - **バランス**: 0 ETH
   - **所有者**: `0x0000000000000000000000000000000000000000`
2. ETHの引き出しはすべて失敗。
3. コントラクトの残高は初期値の `1,000,000,000,000 ETH` に加えて、ウォレット作成時の合計ETHが加算された状態（例: `1,000,000,000,000.5 ETH`）。

---

#### **主な問題点と原因**
1. **`_newWallet` 関数の設計ミス**:
   - 内部的にウォレットを作成する関数が正常に動作せず、すべてのウォレットが同じストレージスロットを共有している可能性がある。
   - ウォレットの所有者とバランスが正しく設定されていないため、ETHを引き出す権利が攻撃者に与えられない。

2. **ウォレットの所有者がゼロアドレス**:
   - `withdraw` 関数を呼び出すためにはウォレットの所有者である必要があるが、所有者が `0x0000000000000000000000000000000000000000` になっているため、攻撃者は引き出しを実行できない。

3. **ウォレットのバランスが0 ETH**:
   - すべてのウォレットのバランスが0 ETHに設定されているため、`withdraw` 関数を呼び出しても引き出し金額が存在しない。

---

#### **エクスプロイトの検討**
スマートコントラクトの設計ミスを利用してエクスプロイトを試みる方法を以下に整理しました。

### **1. ストレージの再利用による所有者変更**
**アイデア**:
- ストレージの再利用を試み、ウォレットの所有者フィールドを攻撃者のアドレスに変更する。
- `0x00` である所有者を自分のアドレスに変更できれば、`withdraw` 関数を実行可能になる。

**課題**:
- Solidityでは、外部からスマートコントラクトのストレージを直接操作することはできない。
- 現在のコードでは、ウォレットの所有者を任意のアドレスに変更する手段が提供されていない。

**結論**:
- この方法は、現在のスマートコントラクトの設計では実現できない。

---

### **2. 再入可能性（Reentrancy）攻撃**
**アイデア**:
- `withdraw` 関数で再入可能性の脆弱性がないか確認する。
- コントラクトの残高を一度にすべて引き出す。

**課題**:
- `withdraw` 関数は`transfer`を使用してETHを送信しており、ガス制限があるため、再入可能性攻撃は不可能。

**結論**:
- この方法も無効。

---

### **3. オーバーフロー/アンダーフロー攻撃**
**アイデア**:
- バランス操作でオーバーフローまたはアンダーフローを発生させ、ウォレットのバランスを操作する。

**課題**:
- Solidity 0.8.xではオーバーフローやアンダーフローがデフォルトでチェックされ、リバートされる。

**結論**:
- この方法は無効。

---

### **4. 外部契約との相互作用**
**アイデア**:
- 攻撃者が別のコントラクトを作成し、`createWallet` や `withdraw` 関数と相互作用させることで脆弱性を突く。

**課題**:
- 現在のスマートコントラクトには、外部コントラクトとのやり取りを通じて新しい脆弱性を利用する余地が見当たらない。

**結論**:
- この方法も現状では困難。

---

#### **エクスプロイトが困難な理由**
1. **所有者の変更ができない**:
   - 所有者フィールドを攻撃者のアドレスに変更する手段がない。
2. **ウォレットのバランスが0 ETH**:
   - 引き出し可能な金額が存在しない。
3. **コントラクトの残高を直接操作する手段がない**:
   - `withdraw` 関数を使用しなければETHを引き出せない。

---

#### **推奨アクション**
1. **スマートコントラクトの設計ミスを分析**:
   - `_newWallet` 関数のバグを深く理解し、スマートコントラクトの設計上の脆弱性を探る。

2. **CTF オーガナイザーへの問い合わせ**:
   - 現在の状況においてエクスプロイトが実現不可能である理由を説明し、追加のヒントを得る。

3. **CTF 特有の脆弱性の探索**:
   - 問題に意図的に設定された脆弱性が存在する可能性があるため、他の未発見の脆弱性を探索。

---

#### **まとめ**
現状のスマートコントラクトの設計では、以下の理由からエクスプロイトを成功させることが困難です：
1. **ウォレットの所有者がゼロアドレスで固定されている。**
2. **ウォレットのバランスが常に0 ETHである。**
3. **コントラクトの残高を直接引き出す手段が存在しない。**



