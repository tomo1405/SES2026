import pytest
from src_0548 import task_func

def test_task_func():
    password = "password"
    salt_length = 8
    encrypted_password = task_func(password, salt_length)
    assert isinstance(encrypted_password, str)
    assert len(encrypted_password) > salt_length