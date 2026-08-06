import pytest
from src_0025 import task_func

def test_task_func_valid_input():
    password = "password123"
    salt, hashed_password = task_func(password)
    assert salt is not None
    assert hashed_password is not None

def test_task_func_invalid_input():
    password = None
    with pytest.raises(ValueError):
        task_func(password)