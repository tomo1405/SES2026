import pytest
from src_0548 import task_func

def test_task_func_with_default_salt_length():
    password = "secure_password"
    result = task_func(password)
    assert isinstance(result, str)
    assert len(result) > len(password)  # Base64 encoded string should be longer than the original password

def test_task_func_with_custom_salt_length():
    password = "another_secure_password"
    salt_length = 16
    result = task_func(password, salt_length)
    assert isinstance(result, str)
    assert len(result) > len(password)

def test_task_func_with_empty_password():
    password = ""
    result = task_func(password)
    assert isinstance(result, str)
    assert len(result) > 0

def test_task_func_with_special_characters():
    password = "!@#$%^&*()"
    result = task_func(password)
    assert isinstance(result, str)
    assert len(result) > len(password)

def test_task_func_with_long_password():
    password = "a" * 1000
    result = task_func(password)
    assert isinstance(result, str)
    assert len(result) > len(password)