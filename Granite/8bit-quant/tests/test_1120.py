import pytest
from src_1120 import task_func
import codecs
import random
import string
import hashlib

def test_task_func():
    password_length = 10
    salt = "salty"
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for i in range(password_length))
    salted_password = (password + salt).encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    result = task_func(password_length, salt)
    assert result == hashed_password

def test_task_func_default_args():
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for i in range(10))
    salted_password = (password + "salty").encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    result = task_func()
    assert result == hashed_password

def test_task_func_invalid_password_length():
    with pytest.raises(ValueError) as excinfo:
        task_func(-1)
    assert "password_length must be a positive integer" in str(excinfo.value)

def test_task_func_invalid_salt():
    with pytest.raises(TypeError) as excinfo:
        task_func(10, 123)
    assert "salt must be a string" in str(excinfo.value)