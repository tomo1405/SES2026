import pytest
from src_0506 import task_func

def test_task_func():
    secret = "my_secret_key"
    message = "Hello, world!"
    expected_output = "a1d0c6e83f027327d8461063f4ac58a6b7c7a23b8fa20a951adbabff9c310a4a"
    assert task_func(secret, message) == expected_output

def test_task_func_empty_secret():
    secret = ""
    message = "Hello, world!"
    expected_output = "f5a7924e621e84c9280a9a27e1bcb7f6a919330e9b62f3079bede767af7a3f34"
    assert task_func(secret, message) == expected_output

def test_task_func_empty_message():
    secret = "my_secret_key"
    message = ""
    expected_output = "5d41402abc4b2a76b9719d911017c592"
    assert task_func(secret, message) == expected_output

def test_task_func_different_secret():
    secret = "another_secret_key"
    message = "Hello, world!"
    expected_output = "d550d8c9b1e5e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1"
    assert task_func(secret, message) == expected_output

def test_task_func_different_message():
    secret = "my_secret_key"
    message = "Goodbye, world!"
    expected_output = "e5e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5b1e5"
    assert task_func(secret, message) == expected_output