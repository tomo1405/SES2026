import pytest
from src_0434 import task_func

def test_task_func_valid_signature():
    s = "SGVsbG8gV29ybGQh"
    signature = "c23d5b7a2e7e8f9e8f9e8f9e8f9e8f9e8f9e8f9e"
    secret_key = "mysecretkey"
    assert task_func(s, signature, secret_key) is True

def test_task_func_invalid_signature():
    s = "SGVsbG8gV29ybGQh"
    signature = "wrongsignature"
    secret_key = "mysecretkey"
    assert task_func(s, signature, secret_key) is False

def test_task_func_empty_string():
    s = ""
    signature = ""
    secret_key = "mysecretkey"
    assert task_func(s, signature, secret_key) is False

def test_task_func_no_secret_key():
    s = "SGVsbG8gV29ybGQh"
    signature = "c23d5b7a2e7e8f9e8f9e8f9e8f9e8f9e8f9e8f9e"
    secret_key = ""
    assert task_func(s, signature, secret_key) is False

def test_task_func_special_characters():
    s = "Hello, World!"
    signature = "c23d5b7a2e7e8f9e8f9e8f9e8f9e8f9e8f9e8f9e"
    secret_key = "!@#$%^&*()"
    assert task_func(s, signature, secret_key) is True