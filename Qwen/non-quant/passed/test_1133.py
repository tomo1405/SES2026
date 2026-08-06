import pytest
from src_1133 import task_func

def test_task_func_with_default_parameters():
    password = "test_password"
    result = task_func(password)
    assert isinstance(result, str)
    assert len(result) > 0

def test_task_func_with_custom_prefix_and_salt_length():
    password = "test_password"
    prefix = "MY"
    salt_length = 32
    result = task_func(password, PREFIX=prefix, SALT_LENGTH=salt_length)
    assert isinstance(result, str)
    assert len(result) > 0

def test_task_func_with_negative_salt_length():
    password = "test_password"
    with pytest.raises(ValueError):
        task_func(password, SALT_LENGTH=-1)

def test_task_func_with_empty_password():
    password = ""
    result = task_func(password)
    assert isinstance(result, str)
    assert len(result) > 0

def test_task_func_with_special_characters():
    password = "!@#$%^&*()"
    result = task_func(password)
    assert isinstance(result, str)
    assert len(result) > 0