python
import hashlib
import hmac
import pytest

def task_func(secret, message):
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()

def test_task_func():
    secret = "secret"
    message = "message"
    expected_result = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    assert task_func(secret, message) == expected_result