plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    code = ord(char)
    code = code + 1
    encrypted_char = chr(code)
    encrypted_text = encrypted_text + encrypted_char

print(plain_text)
print(encrypted_text)
