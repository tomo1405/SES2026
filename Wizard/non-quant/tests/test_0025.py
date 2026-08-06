python
import base64
import hashlib
import os
import pytest

def task_func(password, SALT_LENGTH = 32):
    if not password:
        raise ValueError
    salt = os.urandom(SALT_LENGTH)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.b64encode(salt), base64.b64encode(hashed_password)

def test_task_func():
    with pytest.raises(ValueError):
        task_func('')
    salt, hashed_password = task_func('mypassword')
    assert len(salt) == 44
    assert len(hashed_password) == 98