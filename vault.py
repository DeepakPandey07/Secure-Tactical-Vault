import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def encrypt_file(password, filename):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = kdf.derive(password.encode())
    
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(filename, 'rb') as f:
        data = f.read()
    
    with open(filename + ".enc", 'wb') as f:
        f.write(salt + iv + encryptor.update(data) + encryptor.finalize())
    print(f"File {filename} encrypted successfully.")

# Note for him: Run this to encrypt any sensitive .txt file.