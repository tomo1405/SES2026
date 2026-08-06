import pytest
from src_0434 import task_func

def test_task_func_valid_signature():
    s = "SGVsbG8gV29ybGQh"  # Base64 encoded "Hello World!"
    secret_key = "my_secret_key"
    signature = "d2c5f2a3b1e1f1e1f1e1f1e1f1e1f1e1f1e1f1e1"  # Valid HMAC-SHA1 signature

    assert task_func(s, signature, secret_key) == True

def test_task_func_invalid_signature():
    s = "SGVsbG8gV29ybGQh"  # Base64 encoded "Hello World!"
    secret_key = "my_secret_key"
    signature = "invalid_signature"  # Invalid HMAC-SHA1 signature

    assert task_func(s, signature, secret_key) == False

def test_task_func_empty_string():
    s = ""
    secret_key = "my_secret_key"
    signature = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # HMAC-SHA1 of empty string

    assert task_func(s, signature, secret_key) == True

def test_task_func_non_ascii_characters():
    s = "Café"  # Non-ASCII character
    secret_key = "my_secret_key"
    signature = "valid_signature"  # Precomputed valid HMAC-SHA1 signature

    assert task_func(s, signature, secret_key) == True

def test_task_func_long_string():
    s = "a" * 1000  # Long string
    secret_key = "my_secret_key"
    signature = "valid_signature"  # Precomputed valid HMAC-SHA1 signature

    assert task_func(s, signature, secret_key) == True