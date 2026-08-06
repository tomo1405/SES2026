import pytest
from src_0434 import task_func

def test_task_func():
    s = "Hello, World!"
    signature = "b10a8db164e0754105b7a99be72e3fe5706e2e194"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == True

def test_task_func_invalid_signature():
    s = "Hello, World!"
    signature = "invalid_signature"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == False

def test_task_func_invalid_secret_key():
    s = "Hello, World!"
    signature = "b10a8db164e0754105b7a99be72e3fe5706e2e194"
    secret_key = "invalid_secret_key"
    assert task_func(s, signature, secret_key) == False