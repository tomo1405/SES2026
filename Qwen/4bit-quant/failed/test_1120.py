import pytest
from src_1120 import task_func

def test_task_func_default():
    result = task_func()
    assert isinstance(result, str)
    assert len(result) == 64  # SHA-256 hash length

def test_task_func_custom_length():
    result = task_func(password_length=15)
    assert isinstance(result, str)
    assert len(result) == 64  # SHA-256 hash length

def test_task_func_custom_salt():
    result = task_func(salt="pepper")
    assert isinstance(result, str)
    assert len(result) == 64  # SHA-256 hash length

def test_task_func_reproducibility():
    random.seed(0)
    first_result = task_func()
    random.seed(0)
    second_result = task_func()
    assert first_result == second_result

def test_task_func_encoding():
    result = task_func()
    assert all(c in string.hexdigits for c in result)  # SHA-256 hash should be hexadecimal