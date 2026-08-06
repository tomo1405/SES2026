import pytest
from src_0548 import task_func

def test_task_func_with_default_salt_length():
    password = "securepassword"
    encrypted_password = task_func(password)
    assert isinstance(encrypted_password, str)
    assert len(encrypted_password) > 0

def test_task_func_with_custom_salt_length():
    password = "anothersecurepassword"
    salt_length = 16
    encrypted_password = task_func(password, salt_length)
    assert isinstance(encrypted_password, str)
    assert len(encrypted_password) > 0

def test_task_func_with_empty_password():
    password = ""
    encrypted_password = task_func(password)
    assert isinstance(encrypted_password, str)
    assert len(encrypted_password) > 0

def test_task_func_with_special_characters():
    password = "!@#$%^&*()"
    encrypted_password = task_func(password)
    assert isinstance(encrypted_password, str)
    assert len(encrypted_password) > 0

def test_task_func_with_long_password():
    password = "a" * 1000
    encrypted_password = task_func(password)
    assert isinstance(encrypted_password, str)
    assert len(encrypted_password) > 0