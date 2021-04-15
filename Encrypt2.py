import base64
encoded_data = base64.b64encode("Encode this text")

print("Encoded text with base 64 is")
print(encoded_data)

decoded_data = base64.b64decode("RW5jb2RlIHRoaXMgdGV4dA==")

print("decoded text is ")
print(decoded_data)