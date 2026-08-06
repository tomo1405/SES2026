import pytest
from src_0434 import task_func

def test_task_func_correct_signature():
    s = "SGVsbG8gV29ybGQh"  # Base64 encoded "Hello World!"
    signature = "da39a3ee5e6b4b0d3255bfef95601890af8a103c"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == True

def test_task_func_incorrect_signature():
    s = "SGVsbG8gV29ybGQh"  # Base64 encoded "Hello World!"
    signature = "wrongsignature"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == False

def test_task_func_empty_string():
    s = ""
    signature = "da39a3ee5e6b4b0d3255bfef95601890af8a103c"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == False

def test_task_func_no_secret_key():
    s = "SGVsbG8gV29ybGQh"  # Base64 encoded "Hello World!"
    signature = "da39a3ee5e6b4b0d3255bfef95601890af8a103c"
    secret_key = ""
    assert task_func(s, signature, secret_key) == False

def test_task_func_invalid_base64():
    s = "invalidbase64"
    signature = "da39a3ee5e6b4b0d3255bfef95601890af8a103c"
    secret_key = "secret"
    with pytest.raises(binascii.Error):
        task_func(s, signature, secret_key)