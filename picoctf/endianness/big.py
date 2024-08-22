def to_big_endian(input_string):
    # 文字列をそのままにして、それぞれの文字を16進数に変換
    big_endian = ''.join(f'{ord(char):02X}' for char in input_string)
    return big_endian

input_string = "milri"
big_endian = to_big_endian(input_string)
print(f"Big Endian: {big_endian}")

