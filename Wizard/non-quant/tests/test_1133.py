python
import os
import hashlib
import base64
import pytest

def task_func(password, PREFIX="ME", SALT_LENGTH=16):
    if SALT_LENGTH < 0:
        raise ValueError
    
    salt = os.urandom(SALT_LENGTH)
    salted_password = PREFIX + password + salt.hex()
    
    hashed_password = hashlib.sha256(salted_password.encode()).digest()

    return base64.b64encode(hashed_password).decode()

def test_task_func():
    # Test case 1: Valid input
    assert task_func("password123") == "MEc2h1bmtlczEyMw=="
    
    # Test case 2: Invalid input (SALT_LENGTH < 0)
    with pytest.raises(ValueError):
        task_func("password123", SALT_LENGTH=-1)
    
    # Test case 3: Invalid input (password is None)
    with pytest.raises(TypeError):
        task_func(None)