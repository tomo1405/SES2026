import pytest
from src_1133 import task_func

def test_task_func_with_default_prefix_and_salt_length():
    password = "securepassword"
    expected_prefix = "ME"
    expected_salt_length = 16
    
    result = task_func(password)
    
    assert isinstance(result, str)
    assert len(result) > len(expected_prefix) + len(password) * 2  # Base64 encoding and SHA-256 hash length

def test_task_func_with_custom_prefix_and_salt_length():
    password = "securepassword"
    custom_prefix = "MY"
    custom_salt_length = 8
    
    result = task_func(password, PREFIX=custom_prefix, SALT_LENGTH=custom_salt_length)
    
    assert isinstance(result, str)
    assert len(result) > len(custom_prefix) + len(password) * 2  # Base64 encoding and SHA-256 hash length

def test_task_func_with_negative_salt_length():
    password = "securepassword"
    negative_salt_length = -1
    
    with pytest.raises(ValueError):
        task_func(password, SALT_LENGTH=negative_salt_length)

def test_task_func_with_empty_password():
    password = ""
    expected_prefix = "ME"
    expected_salt_length = 16
    
    result = task_func(password)
    
    assert isinstance(result, str)
    assert len(result) > len(expected_prefix) + expected_salt_length * 2  # Base64 encoding and SHA-256 hash length

def test_task_func_with_special_characters():
    password = "!@#$%^&*()"
    expected_prefix = "ME"
    expected_salt_length = 16
    
    result = task_func(password)
    
    assert isinstance(result, str)
    assert len(result) > len(expected_prefix) + len(password) * 2  # Base64 encoding and SHA-256 hash length