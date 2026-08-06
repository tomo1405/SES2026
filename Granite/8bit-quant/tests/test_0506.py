import hashlib
import hmac
import pytest

from src_0506 import task_func

def test_task_func():
    secret = "my_secret_key"
    message = "hello, world!"
    expected_result = "b5d89c50c665611c8657742eb1e4f1f0e9f0d8817a3952d15e59f44715e4838b"

    result = task_func(secret, message)

    assert result == expected_result