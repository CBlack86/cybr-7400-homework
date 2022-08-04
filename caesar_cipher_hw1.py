def encrypt(text, e_key,):
    e_str = ""
    for t in text:
        if t==chr(32):
            e_str+=t
        if t.isupper():
            change = 65 + ((ord(t) - 65 + e_key) % 26)
            e_str += chr(change)
        elif t.islower():
            change = 97 + ((ord(t) - 97 + e_key) % 26)
            e_str += chr(change)
    return e_str

def decrypt(e_text, e_key):
    d_str = ""
    for t in e_text:
        if t==chr(32):
            d_str+=t
        if t.isupper():
            if ((ord(t) - 65 - e_key) < 0):
                change = 65 + ((ord(t) - 65 - e_key + 26) % 26)
            else:
                change = 65 + ((ord(t) - 65 - e_key) % 26)
            d_str += chr(change)
        elif t.islower():
            if ((ord(t) - 97 - e_key) <0):
                change = 97 + ((ord(t) - 97 - e_key + 26) % 26)
            else:
                change = 97 + ((ord(t) - 97 - e_key) % 26)
            d_str += chr(change)
    return d_str

e_key = int(input("Enter your encryption key: "))
text = str(input("Enter your message: "))
e_text = encrypt(text, e_key)
d_text = decrypt(e_text, e_key)
print("Your encrypted message is: ", e_text.upper())
print("Your decrypted message is: ", d_text)
