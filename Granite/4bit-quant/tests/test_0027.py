import base64
from cryptography.fernet import Fernet
from src_0027 import task_func
import pytest

def test_task_func():
    message = "This is a secret message"
    encryption_key = b"your_encryption_key_here"
    encrypted_message = task_func(message, encryption_key)
    assert isinstance(encrypted_message, str)
    assert len(encrypted_message) > 0
    assert encrypted_message != message