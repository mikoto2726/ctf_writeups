import os
import hashlib
import itertools

def xor(key, data):
    return bytes([k^d for k, d in zip(itertools.cycle(key),data)])

def decrypt(phrase, encrypted, iters=1000):
    key = phrase.encode()
    for _ in range(iters):
        key = hashlib.md5(key).digest()
    for _ in range(iters):
        encrypted = xor(key, encrypted)
        key = hashlib.md5(key).digest()
    return encrypted

encrypted_flag_hex = "6db78706159d22"
encrypted_flag = bytes.fromhex(encrypted_flag_hex)
phrase = os.environ.get('FLAG', 'missing')


flag = decrypt(phrase, encrypted_flag)
print(flag)

# バイナリデータを16進数で表示
print(flag.hex())

# 可能なエンコーディングを試してみる
try:
    print(flag.decode('latin1'))
except UnicodeDecodeError:
    print("Cannot decode with latin1")

try:
    print(flag.decode('iso-8859-1'))
except UnicodeDecodeError:
    print("Cannot decode with iso-8859-1")

try:
    print(flag.decode('utf-16'))
except UnicodeDecodeError:
    print("Cannot decode with utf-16")





