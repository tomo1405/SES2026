import base64
from cryptography.fernet import Fernet
def task_func(message, encryption_key):
    fernet = Fernet(base64.urlsafe_b64encode(encryption_key.encode()))
    encrypted_message = fernet.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()