
#!/usr/bin/env python3
import sys
from Crypto.Util.number import bytes_to_long, long_to_bytes

# ==============
# サーバ側の想定（関数）
# ==============
# ここでは問題文の encrypt/decrypt と同等の関数があると仮定
# （実際の攻撃はサーバのメニュー操作を自動化 or 手動でやる）
def oracle_encrypt(msg_bytes) -> int:
    # サーバ側で: bytes_to_long(msg_bytes)^e mod N
    # ただし msg_bytes に b"katagaitai-CTF" が含まれると拒否
    # (ここでは簡略化して ValueError を投げる)
    if b"katagaitai-CTF" in msg_bytes:
        raise ValueError("Contains restricted words!")
    return pow(bytes_to_long(msg_bytes), e, N)

def oracle_decrypt(cipher_int: int) -> bytes:
    # サーバ側で: cipher_int^d mod N → bytes
    # 実際の問題ではこれを復号結果と比較して
    # 一致すれば FLAG を表示、違えば "Bad!"
    m_int = pow(cipher_int, d, N)
    return long_to_bytes(m_int)

# ==============
# 攻撃スクリプト
# ==============
def attack():
    # 1) 禁止平文 "katagaitai-CTF" の整数値を求める
    M_bytes = b"katagaitai-CTF"
    M_int = bytes_to_long(M_bytes)
    print(f"[+] M_int = {M_int}")

    # 2) 小さい m1 を適当に選ぶ (例: m1 = 2)
    #    M_int が偶数であれば M_int // 2 が整数になる
    #    ※ もし M_int が偶数でなかったら、m1=3,5,... と試すなど工夫する
    m1_int = 2
    if M_int % m1_int != 0:
        print("[!] M is not divisible by 2... try other small integers or approach.")
        sys.exit(1)

    m2_int = M_int // m1_int  # これで m1_int * m2_int = M_int

    # 3) バイト列化して禁止キーワードチェック
    m1_bytes = long_to_bytes(m1_int)
    m2_bytes = long_to_bytes(m2_int)
    if b"katagaitai-CTF" in m1_bytes or b"katagaitai-CTF" in m2_bytes:
        print("[!] Unexpectedly found restricted substring in m1 or m2. Try another approach.")
        sys.exit(1)

    # 4) サーバの encrypt() 相当を呼び出して c1, c2 を取得
    try:
        c1_int = oracle_encrypt(m1_bytes)
        c2_int = oracle_encrypt(m2_bytes)
    except ValueError as e:
        print("[!] Oracle rejected input. Try different m1.")
        sys.exit(1)

    # 5) c_m = c1_int * c2_int (普通の整数乗算)
    #    後の decrypt で c_m^d mod N が計算されるから大丈夫
    c_m_int = c1_int * c2_int

    # 6) decrypt() に c_m_int を送って、ちゃんと b"katagaitai-CTF" に戻るか確認
    decrypted = oracle_decrypt(c_m_int)
    if decrypted == M_bytes:
        print("[+] Success! The server would output FLAG here.")
    else:
        print("[!] Something went wrong. Check your steps.")

# ==========
# メイン
# ==========
if __name__ == "__main__":
    # (実際にはサーバで p,q が固定されるが、ここはデモ用にランダム生成)
    from Crypto.Util.number import getStrongPrime, inverse
    p = getStrongPrime(1024)
    q = getStrongPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    e = 0x10001
    d = inverse(e, phi)

    attack()
