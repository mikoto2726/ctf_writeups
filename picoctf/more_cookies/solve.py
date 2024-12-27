
import requests
import base64

# サーバーのURL
url = "http://mercury.picoctf.net:21553/"

# オリジナルのCookie
original_cookie = "amFLZURTMzJ6cEZObEhXTHdGZFY2MEpxMDlzOWJKdHRqZXZVUXFWS1BtRElSSlBmTDVycmsweWUySWRZQUZUZmFtekhFSUxIdjlQLzA2TkpNWjFmek1uRlZiZUVxb0JFS2lianJBZmhDVVFKN2wxMUo5MkJPYXlLcnVWc2wyZ1k="

# Base64デコードしてバイト列に変換
cipher_bytes = base64.b64decode(original_cookie)

# 暗号文を改ざん
for i in range(len(cipher_bytes)):
    for bit in range(8):
        modified_bytes = bytearray(cipher_bytes)
        modified_bytes[i] ^= (1 << bit)  # i番目のブロックの特定ビットをフリップ

        # Base64エンコードしてCookieとして送信
        modified_cookie = base64.b64encode(modified_bytes).decode('utf-8')
        cookies = {'auth_name': modified_cookie}

        # サーバーにリクエストを送信
        response = requests.get(url, cookies=cookies)

        # 成功した場合、フラグが含まれるレスポンスが返ってくる
        if "picoCTF{" in response.text:
            print("Flag found:", response.text)
            exit()
