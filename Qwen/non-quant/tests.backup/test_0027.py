import pytest
from src_0027 import task_func

def test_task_func():
    # Test with a simple message and key
    message = "Hello, World!"
    encryption_key = "secretkey123"
    expected_output = "gAAAAABf..."
    
    assert task_func(message, encryption_key) == expected_output

def test_task_func_empty_message():
    # Test with an empty message
    message = ""
    encryption_key = "secretkey123"
    expected_output = "gAAAAABf..."
    
    assert task_func(message, encryption_key) == expected_output

def test_task_func_empty_key():
    # Test with an empty encryption key
    message = "Hello, World!"
    encryption_key = ""
    with pytest.raises(ValueError):
        task_func(message, encryption_key)

def test_task_func_special_characters():
    # Test with special characters in the message
    message = "!@#$%^&*()"
    encryption_key = "secretkey123"
    expected_output = "gAAAAABf..."
    
    assert task_func(message, encryption_key) == expected_output

def test_task_func_long_message():
    # Test with a long message
    message = "a" * 1000
    encryption_key = "secretkey123"
    expected_output = "gAAAAABf..."
    
    assert task_func(message, encryption_key) == expected_output

def test_task_func_long_key():
    # Test with a long encryption key
    message = "Hello, World!"
    encryption_key = "a" * 100
    expected_output = "gAAAAABf..."
    
    assert task_func(message, encryption_key) == expected_output