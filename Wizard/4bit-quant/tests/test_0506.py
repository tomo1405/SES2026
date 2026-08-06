python
import hashlib
import hmac
import pytest

def task_func(secret, message):
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()

def test_task_func():
    secret = "secret"
    message = "message"
    expected_result = "a1d5a7d5c8d5d8d5d8d5d8d5d8d5d8d5d8d5d8d5d8d5d8d5d8d5d8d5d8d5d8"
    assert task_func(secret, message) == expected_result