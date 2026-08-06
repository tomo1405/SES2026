import pytest
from src_0434 import task_func

def test_task_func():
    s = "Hello, World!"
    signature = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    secret_key = "my_secret_key"
    assert task_func(s, signature, secret_key) == True

    s = "Goodbye, World!"
    signature = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    secret_key = "my_secret_key"
    assert task_func(s, signature, secret_key) == False

    s = "Hello, World!"
    signature = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    secret_key = "my_secret_key"
    assert task_func(s, signature, secret_key) == True

    s = "Goodbye, World!"
    signature = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    secret_key = "my_secret_key"
    assert task_func(s, signature, secret_key) == False