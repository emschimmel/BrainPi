import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class PasswordHelper:

    @staticmethod
    def hashPassword(password):
        password = str.encode(password)
        salt = b'this is my salty little secret'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key


    @staticmethod
    def encryptPassword(key):
        f = Fernet(key)
        token = f.encrypt(key)
        return token
