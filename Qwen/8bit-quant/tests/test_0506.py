import pytest
from src_0506 import task_func

def test_task_func_with_valid_inputs():
    secret = "my_secret_key"
    message = "Hello, World!"
    expected_output = "a1d0c6e83f027327d8461063f4ac58a6b7c7a23b8fa20a951adbabff9c310a4a"
    assert task_func(secret, message) == expected_output

def test_task_func_with_empty_secret():
    secret = ""
    message = "Hello, World!"
    expected_output = "b10a8db164e0754105b7a99be72e3fe5305540e336770a7c52b1e5c042f772fb"
    assert task_func(secret, message) == expected_output

def test_task_func_with_empty_message():
    secret = "my_secret_key"
    message = ""
    expected_output = "f2c1b1e1b1e1b1e1b1e1b1e1b1e1b1e1b1e1b1e1b1e1b1e1b1e1b1e1b1e1b1e1"
    assert task_func(secret, message) == expected_output

def test_task_func_with_special_characters():
    secret = "!@#$%^&*()"
    message = "Special chars: !@#$%^&*()"
    expected_output = "b10a8db164e0754105b7a99be72e3fe5305540e336770a7c52b1e5c042f772fb"
    assert task_func(secret, message) == expected_output

def test_task_func_with_unicode_characters():
    secret = "my_secret_key"
    message = "こんにちは、世界！"
    expected_output = "b10a8db164e0754105b7a99be72e3fe5305540e336770a7c52b1e5c042f772fb"
    assert task_func(secret, message) == expected_output