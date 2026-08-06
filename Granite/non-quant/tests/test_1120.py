import pytest
from src_1120 import task_func

def test_task_func():
    password_length = 10
    salt = "salty"
    hashed_password = task_func(password_length, salt)
    assert isinstance(hashed_password, str)
    assert len(hashed_password) == 64