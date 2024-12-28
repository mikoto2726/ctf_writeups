import base64

token = "cGljb0NURntqQmhEMnk3WG9OelB2XzFZeFM5RXc1cUwwdUk2cGFzcWxfaW5qZWN0aW9uXzI1YmE0ZGUxfQ=="

flag = base64.b64decode(token).decode('utf-8')
print(flag)
