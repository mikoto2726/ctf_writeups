with open('enc', 'r') as f:
    enc = f.read()

flag = ''
for ch in enc:
    flag += chr(ord(ch) >> 8) + chr(ord(ch) & 0xff)

print(flag)
