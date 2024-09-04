password = 1634668422544022562287275254811184478161245548888973650857381112077711852144181630709254123963471597994127621183174673720047559236204808750789430675058597

password2 = 2 * password

print("password2:", password2)

decrypted_hex = "764cda2a147a9f3787dcc2350277e811e8524991108acc756df205d8b1b61bdcabce1e36704188ba050fa2061364addb38fafa67cb3e46b2ed3820235aaf63"


# 16進数を整数に変換
decrypted_number = int(decrypted_hex, 16)

print("Decrypted Number:", decrypted_number)

# 2で割る
original_password_number = decrypted_number // 2
# 16進数に変換
original_password_hex = hex(original_password_number)[2:]

# バイト列に変換
original_password_bytes = bytes.fromhex(original_password_hex)

# ASCII文字列に変換
original_password = original_password_bytes.decode('ascii', errors='ignore')

print("Original Password:", original_password)

print("Original Password Number:", original_password_number)

original_password_hex = hex(12101336763675166531745807502018440543779689406989660004941115504664543290340952392831864717098927496357982431964096079804310110400394341506943535634353)[2:]
print("Original Password Hex:", original_password_hex)

original_password_bytes = bytes.fromhex(original_password_hex)
original_password = original_password_bytes.decode('ascii', errors='ignore')
print("Original Password (ASCII):", original_password)

# 16進数をそのままバイト列に変換し、表示できない部分も含めて表示
original_password_bytes = bytes.fromhex("3b266d150a3d4f9bc3ee611a813bf408f42924c88845663ab6f902ec58db0dee55e70f1b3820c45d0287d10309b256ed9c7d7d33e59f2359769c1011ad57b1")

# 表示できる部分だけを抽出
print("Original Password (Raw Bytes):", original_password_bytes)

# 表示できる文字のみを抽出して表示
original_password_cleaned = original_password_bytes.decode('ascii', errors='replace')
print("Original Password (Cleaned):", original_password_cleaned)


from Crypto.Cipher import AES

# 復号に使用するバイト形式のパスワード
password = b';&m\x15\n=O\x9b\xc3\xeea\x1a\x81;\xf4\x08\xf4)$\xc8\x88Ef:\xb6\xf9\x02\xecX\xdb\r\xeeU\xe7\x0f\x1b8 \xc4]\x02\x87\xd1\x03\t\xb2V\xed\x9c}}3\xe5\x9f#Yv\x9c\x10\x11\xadW\xb1'

# AES-256復号のための設定
cipher = AES.new(password, AES.MODE_CBC, iv)  # iv (初期ベクトル)も適切に設定する必要があります
with open('secret.enc', 'rb') as f:
    encrypted_data = f.read()

# 復号処理
decrypted_data = cipher.decrypt(encrypted_data)

# 復号されたメッセージを表示または保存
print(decrypted_data.decode('utf-8', errors='ignore'))


