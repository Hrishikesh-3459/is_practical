# Write a Java/C/C++/Python program to implement AES Algorithm.

# pip install pycrypto


import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

secret_key = input("Enter the key: ")

block_size = AES.block_size
key = hashlib.sha256(secret_key.encode()).digest()

def encrypt(plain_text):
    plain_text = pad(plain_text)
    iv = Random.new().read(block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_text = cipher.encrypt(plain_text.encode())
    return b64encode(iv + encrypted_text).decode("utf-8")

def decrypt(encrypted_text):
    encrypted_text = b64decode(encrypted_text)
    iv = encrypted_text[:block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = cipher.decrypt(encrypted_text[block_size:]).decode("utf-8")
    return unpad(plain_text)

def pad(plain_text):
    number_of_bytes_to_pad = block_size - len(plain_text) % block_size
    ascii_string = chr(number_of_bytes_to_pad)
    padding_str = number_of_bytes_to_pad * ascii_string
    padded_plain_text = plain_text + padding_str
    return padded_plain_text

def unpad(plain_text):
    last_character = plain_text[len(plain_text) - 1:]
    return plain_text[:-ord(last_character)]

try:
    decision = int(input("Enter 1 to encrypt Plain Text, 2 to decrypt Cipher Text: "))
    if decision == 1:
        plainText = input("Please enter plain text: ")
        print("Cipher Text = ", encrypt(plainText))

    elif decision == 2:
        cipherText = input("Please enter cipher text: ")
        print("Plain Text = ", decrypt(cipherText))

    else:
        print("Incorrect input")
except:
    print("Incorrect input or secret key")