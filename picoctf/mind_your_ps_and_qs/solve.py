from sympy import mod_inverse

# 与えられたRSA暗号の値
c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537

# factordbで得られたpとqの値をここに入力
p = 1617549722683965197900599011412144490161 # 例として入力
q = 475693130177488446807040098678772442581573  # 例として入力

# φ(n) を計算 (φ(n) = (p-1)*(q-1))
phi = (p - 1) * (q - 1)

# 秘密鍵 d を計算 (d = eの逆元 mod φ(n))
d = mod_inverse(e, phi)

# 復号化 (plaintext = c^d mod n)
plaintext = pow(c, d, n)

# 復号化されたメッセージを数値から文字列に変換して出力
decrypted_message = bytearray.fromhex(hex(plaintext)[2:]).decode()
print(f"Decrypted text: {decrypted_message}")

