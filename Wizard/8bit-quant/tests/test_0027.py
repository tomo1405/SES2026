python
import base64
import pytest
from cryptography.fernet import Fernet

def task_func(message, encryption_key):
    fernet = Fernet(base64.urlsafe_b64encode(encryption_key.encode()))
    encrypted_message = fernet.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()

def test_task_func():
    message = "Hello, world!"
    encryption_key = "secret_key"
    encrypted_message = task_func(message, encryption_key)
    assert encrypted_message != message
    assert encrypted_message != encryption_key