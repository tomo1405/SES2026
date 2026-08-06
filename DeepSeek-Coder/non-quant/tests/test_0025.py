import pytest
from src_0025 import task_func

def test_task_func_valid_input():
    password = "test_password"
    salt, hashed_password = task_func(password)
    assert isinstance(salt, bytes)
    assert isinstance(hashed_password, bytes)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func("")