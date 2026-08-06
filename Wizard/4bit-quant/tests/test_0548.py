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
    # Test case 1: Valid password and salt length
    assert task_func('password123', 8) == 'c2FsdDEyMyBzY2hlbWE='

    # Test case 2: Password with special characters and salt length of 16
    assert task_func('P@ssw0rd!', 16) == 'c2FsdDEyMyBzY2hlbWE='

    # Test case 3: Password with uppercase letters and salt length of 32
    assert task_func('PASSWORD123', 32) == 'c2FsdDEyMyBzY2hlbWE='

    # Test case 4: Password with lowercase letters and salt length of 64
    assert task_func('password123', 64) == 'c2FsdDEyMyBzY2hlbWE='

    # Test case 5: Password with numbers and salt length of 128
    assert task_func('1234567890', 128) == 'c2FsdDEyMyBzY2hlbWE='

    # Test case 6: Password with all characters and salt length of 256
    assert task_func('!@#$%^&*()_+-=[]{}|;:,.<>?', 256) == 'c2FsdDEyMyBzY2hlbWE='

    # Test case 7: Password with length 0 and salt length of 1
    with pytest.raises(ValueError):
        task_func('', 1)

    # Test case 8: Password with length 100 and salt length of 100
    with pytest.raises(ValueError):
        task_func('a' * 100, 100)

    # Test case 9: Salt length of 0
    with pytest.raises(ValueError):
        task_func('password123', 0)

    # Test case 10: Salt length of 100
    with pytest.raises(ValueError):
        task_func('password123', 100)