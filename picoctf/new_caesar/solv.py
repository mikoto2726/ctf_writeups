import string

LOWERCASE_OFFSET = ord("a") # 97
ALPHABET = string.ascii_lowercase[:16] # abcdefghijklmnop

cipher = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"

# b16_encodeをデコードする関数
def b16_decode(cipher):
    plain = ""
    li_cipher = [(i+j) for i, j in zip(cipher[::2], cipher[1::2])]
    for c in li_cipher:
        u = '{:08b}'.format(ALPHABET.index(c[0]))[4:]
        l = '{:08b}'.format(ALPHABET.index(c[1]))[4:]
        plain += chr(int(u+l, 2))    
    return plain

# shiftの逆関数
def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

for key in ALPHABET:
    shifted = ""
    for i, c in enumerate(cipher):
        shifted += unshift(c, key[i % len(key)])
    flag = b16_decode(shifted)
    print('key:', key, 'flag:', flag)

