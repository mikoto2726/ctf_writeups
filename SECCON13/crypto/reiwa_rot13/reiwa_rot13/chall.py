from Crypto.Util.number import *
import codecs
import string
import random
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from flag import flag

# Get a strong prime number
p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q
e = 137

# Generate a random key and its rot13
key = ''.join(random.sample(string.ascii_lowercase, 10))
rot13_key = codecs.encode(key, 'rot13')

# Encrypt the keys
key = key.encode()
rot13_key = rot13_key.encode()

print("n =", n)
print("e =", e)
print("c1 =", pow(bytes_to_long(key), e, n))
print("c2 =", pow(bytes_to_long(rot13_key), e, n))

# Encrypt the flag
key = hashlib.sha256(key).digest()
cipher = AES.new(key, AES.MODE_ECB)
print("encyprted_flag = ", cipher.encrypt(flag))