from flag import FLAG
from Crypto.Util.number import *

MENU = """
1. Encryption.
2. Decryption.
3. Exit.
"""

# 平文を暗号化する関数
def encrypt(e, N):
    # 16進数形式でデータの入力を受け付けて、bytes型に変換
    try:
        message = bytes.fromhex(input("input your message (hex)> "))
    except Exception as e:
        print(e)
        print("Bye!!")
        exit(1)
    
    # データに "katagaitai-CTF"が含まれていないかチェック
    if b"katagaitai-CTF" in message:
        print("Contains restricted words!")
        return
    
    cipher = hex(pow(bytes_to_long(message), e, N))[2:]
    print(cipher)

# 暗号文を復号する関数
def decrypt(d, N):
    # 16進数形式で暗号文の入力を受け付けて、bytes型に変換
    try:
        cipher = input("input your cipher (hex)> ")
    except Exception as e:
        print(e)
        print("Bye!!")
        exit(1)

    c = int(cipher, 16)
    data = long_to_bytes(pow(c, d, N))
    
    # 暗号文の復号結果がkatagaitai-CTFの場合、FLAGを表示
    if data == b"katagaitai-CTF":
        print("Great!")
        print(f"FLAG is {FLAG}")
    else:
        print("Bad!")

def main():
    p = getStrongPrime(1024)
    q = getStrongPrime(1024)
    N = p * q
    phi = (p - 1) * (q - 1)
    e = 0x10001
    d = inverse(e, phi)
    
    print("=== Oracle Service1 ===\n")
    print(f"N = {N}")
    
    while True:
        print(MENU)
        choice = input("> ")
        if choice not in ["1", "2"]:
            print("Bye!!")
            exit(0)
            break
        if choice == "1":
            encrypt(e, N)
        if choice == "2":
            decrypt(d, N)
    
if __name__ == '__main__':
    main()
