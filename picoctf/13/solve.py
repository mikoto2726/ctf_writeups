def rot13(text):
    result = []
    for char in text:
        # 大文字の場合
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        # 小文字の場合
        elif 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        else:
            result.append(char)  # アルファベット以外の文字はそのまま
    return ''.join(result)

# 使用例
encrypted_text = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
decrypted_text = rot13(encrypted_text)
print(decrypted_text)

