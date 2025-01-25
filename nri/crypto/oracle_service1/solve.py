
import os
import sys
import random
from Crypto.Util.number import bytes_to_long, long_to_bytes
from math import gcd

####################################
# ここは問題文の Oracle と
# 同等の関数を想定したダミー
####################################
def oracle_encrypt(msg_bytes) -> int:
    """
    問題文にある encrypt() 関数を呼ぶのと同等とみなす。
    msg_bytes を hex 変換して送る。
    戻り値は pow(bytes_to_long(msg_bytes), e, N) の整数。
    ただし msg_bytes に b"katagaitai-CTF" が含まれているときは失敗する。
    """
    if b"katagaitai-CTF" in msg_bytes:
        raise ValueError("Contains restricted words!")
    return pow(bytes_to_long(msg_bytes), e, N)

def oracle_decrypt(cipher_int: int):
    """
    問題文にある decrypt() 関数を呼ぶのと同等。
    cipher_int を hex 変換して送る。
    戻り値は平文の bytes。
    もし b"katagaitai-CTF" なら FLAG が表示される(問題文の挙動)。
    ここでは擬似的に戻り値をそのまま返す、とだけする。
    """
    plaintext = pow(cipher_int, d, N)
    return long_to_bytes(plaintext)

####################################
# ここから実際の攻撃手順
####################################

# ===== 1) セットアップ =====
# ここでは問題の main() 内で得られる N, e, d を想定しているが
# 実際には print される N を取得し、あとは Oracle への問い合わせで暗号化/復号を行う。
# （攻撃者は d は知らないが、ここは例示のため置いている）
p = 0  # 本来はサーバ側のみが知る
q = 0

N = 30874125707869794473990147802093416276737833279170263042508837555717459073877316423702385469716422998363841272325763587849217054781450812655413801872429442525648445183986390980697392640825144823887603082144774501162608001051887326873775091042925889714331589749272358717764755581017494660826670597706556362545950722251782673476948794350092086236167505929749335537553132843272097776697044952768643718641199071735354438695739139122227954494188962690621801999784483581271757959412201182764556524178994308170099709367730624198329687019397774141821483113336012172587783515636632905420811619213249241089019598350935413989729
e = 0x10001
d = 0  # 攻撃者は本来知らない

# ==== 攻撃者の知りたい禁止平文 ====
M_bytes = b"katagaitai-CTF"
M_int = bytes_to_long(M_bytes)

# 実際のスクリプトではここで N, e を使い、以下の手順だけ実行:
def attack_forbidden_plaintext(N, e):
    while True:
        # 2) ランダムな r を生成して整数化
        #    なるべく N より小さくなるように random で生成
        #    （もっと安全にやるなら os.urandom(256) とかで大きな乱数をとるなど）
        r_int = random.randrange(2, N)
        if gcd(r_int, N) != 1:
            continue

        # 3) r の逆元を計算 (r_inv = r^{-1} mod N)
        #    ここでは pow(r_int, -1, N) (Python 3.8+)
        try:
            r_inv_int = pow(r_int, -1, N)
        except ValueError:
            continue  # 逆元が存在しない(= gcd != 1)ならやり直し

        # 4) X = M * r_inv mod N
        X_int = (M_int * r_inv_int) % N
        X_bytes = long_to_bytes(X_int)

        # X_bytes に禁止ワードが含まれないかチェック
        if b"katagaitai-CTF" in X_bytes:
            # まれに衝突したらやり直し
            continue

        # === ここまで来たら X, r の両方とも禁止ワードを含まないはず ===
        try:
            cX_int = oracle_encrypt(X_bytes)  # Enc(X)
            cR_int = oracle_encrypt(long_to_bytes(r_int))  # Enc(r)
        except ValueError:
            # 何らかの理由で弾かれたらやり直し
            continue

        # 5) cM = cX * cR mod N = Enc(M)
        cM_int = (cX_int * cR_int) % N
        return cM_int

def main_attack():
    # (実際は手動で N をコピーするなどして、e=65537 と併用)
    cM_int = attack_forbidden_plaintext(N, e)

    # この cM_int を 16 進数表示して、Oracle の decrypt(d, N) に与える
    print("[+] The forged ciphertext for 'katagaitai-CTF' is:", hex(cM_int)[2:])
    print("Now send it to the decrypt function to get the FLAG!")

# 実行
if __name__ == "__main__":
    main_attack()
