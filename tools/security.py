from cryptography.fernet import Fernet
import os

def generateSecurityKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return os.getenv("SALT")

def crypt(data):
    f = Fernet(load_key())
    return f.encrypt(data.encode())

def decrypt(data):
    f = Fernet(load_key())
    return f.decrypt(data).decode()