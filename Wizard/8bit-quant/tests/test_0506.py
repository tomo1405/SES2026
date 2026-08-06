python
import hashlib
import hmac
import pytest

def task_func(secret, message):
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()

def test_task_func():
    secret = "secret"
    message = "message"
    expected_result = "a94a110d86d24934e502a7c8294c1e6e5a55555555555555555555555555555"
    assert task_func(secret, message) == expected_result