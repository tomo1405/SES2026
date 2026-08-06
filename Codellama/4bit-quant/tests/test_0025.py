import pytest
from src_0025 import task_func

def test_task_func():
    password = "password123"
    salt, hashed_password = task_func(password)
    assert salt == b"salt"
    assert hashed_password == b"hashed_password"

def test_task_func_empty_password():
    password = ""
    with pytest.raises(ValueError):
        task_func(password)

def test_task_func_invalid_password():
    password = "password123"
    with pytest.raises(ValueError):
        task_func(password)

def test_task_func_invalid_salt_length():
    password = "password123"
    with pytest.raises(ValueError):
        task_func(password, SALT_LENGTH=0)