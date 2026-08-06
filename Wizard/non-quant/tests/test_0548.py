python
import hashlib
import os
import base64
import pytest

def task_func(password: str, salt_length: int = 8) -> str:
    # Generate a random salt
    salt = os.urandom(salt_length)
    # Use the salt and the password to create a SHA-256 hash
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Combine the salt and the hash
    salted_hash = salt + hash
    # Encode the salted hash in base64
    encrypted_password = base64.b64encode(salted_hash)

    return encrypted_password.decode('utf-8')

def test_task_func():
    # Test case 1: Test with default salt length
    assert task_func('password') == 'cGFzc3dvcmQ='

    # Test case 2: Test with custom salt length
    assert task_func('password', salt_length=16) == 'cGFzc3dvcmQ='