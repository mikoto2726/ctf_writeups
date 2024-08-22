def to_little_endian(input_string):
    # 文字列を逆順にし、それぞれの文字を16進数に変換
    little_endian = ''.join(f'{ord(char):02X}' for char in reversed(input_string))
    return little_endian

input_string = "milri"
little_endian = to_little_endian(input_string)
print(f"Little Endian: {little_endian}")

