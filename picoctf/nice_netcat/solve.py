key = ""
with open("key.txt", "r") as file:
    for line in file.readlines():
        stripped_line = line.strip()
        if stripped_line:  # 空行でないことを確認
            key += chr(int(stripped_line))
    print(key)

