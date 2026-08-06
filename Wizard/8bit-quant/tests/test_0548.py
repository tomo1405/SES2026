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
    # Test case 1: Valid input
    assert task_func('password123') == 'c2FsdHlfMTIz'

    # Test case 2: Invalid input (empty string)
    with pytest.raises(ValueError):
        task_func('')

    # Test case 3: Invalid input (None)
    with pytest.raises(TypeError):
        task_func(None)

    # Test case 4: Invalid input (non-string)
    with pytest.raises(TypeError):
        task_func(12345)

    # Test case 5: Invalid input (salt_length < 0)
    with pytest.raises(ValueError):
        task_func('password123', -1)

    # Test case 6: Invalid input (salt_length > 1000)
    with pytest.raises(ValueError):
        task_func('password123', 1001)