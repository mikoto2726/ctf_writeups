import string

LOWERCASE_OFFSET = ord("a") # 97
ALPHABET = string.ascii_lowercase[:16] # abcdefghijklmnop

def b16_encode(plain): # 8-bit to 4-bit encoding
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c)) # 8-bit binary
        enc += ALPHABET[int(binary[:4], 2)] # first 4 bits
        enc += ALPHABET[int(binary[4:], 2)] # last 4 bits
    return enc

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET # 0-indexed
    t2 = ord(k) - LOWERCASE_OFFSET # 0-indexed
    return ALPHABET[(t1 + t2) % len(ALPHABET)] # circular shift

flag = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"
for i in range  (0, 16):
    key = ALPHABET[i]
    assert all([k in ALPHABET for k in key]) # key is in ALPHABET
    assert len(key) == 1    
    b16 = b16_encode(flag)
    enc = ""
    for i, c in enumerate(b16): # encrypt
        enc += shift(c, key[i % len(key)]) # repeating key
        if "pico" in enc: # flag format
            print(enc)
            break
