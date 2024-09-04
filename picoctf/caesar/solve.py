def caesar_cipher(text, shift):
    result = ""
    
    # 各文字を処理
    for char in text:
        # 文字がアルファベットかどうかを確認
        if char.isalpha():
            # 大文字か小文字かを確認し、アルファベットの範囲に変換
            start = ord('A') if char.isupper() else ord('a')
            # シフトの計算
            shifted = (ord(char) - start + shift) % 26 + start
            # 結果に追加
            result += chr(shifted)
        else:
            # アルファベットでない場合はそのまま結果に追加
            result += char
    
    return result

def try_all_shifts(encrypted_text):
    for shift in range(26):
        decrypted_text = caesar_cipher(encrypted_text, -shift)
        print(f"Shift {shift}: {decrypted_text}")

# 使用例
encrypted_text = "dspttjohuifsvcjdpoabrkttds"

# 全シフトを試す
try_all_shifts(encrypted_text)

