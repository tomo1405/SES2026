import hashlib
import hmac
import pytest

from src_0506 import task_func

def test_task_func():
    secret = "my_secret"
    message = "my_message"
    expected_result = "8e67f6b7f368f1d3a9d1c1d1c1d1c1d1c1d1c1d1c1d1c1d1c1d1c1d1c1d1c1d1"
    result = task_func(secret, message)
    assert result == expected_result

def test_task_func_with_empty_secret():
    secret = ""
    message = "my_message"
    with pytest.raises(ValueError):
        task_func(secret, message)

def test_task_func_with_empty_message():
    secret = "my_secret"
    message = ""
    with pytest.raises(ValueError):
        task_func(secret, message)