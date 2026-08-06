import pytest
from src_0434 import task_func

def test_task_func():
    s = "Hello, World!"
    signature = "1234567890abcdef"
    secret_key = "my_secret_key"
    assert task_func(s, signature, secret_key) == True

    s = "Goodbye, World!"
    signature = "abcdef1234567890"
    secret_key = "my_secret_key"
    assert task_func(s, signature, secret_key) == False