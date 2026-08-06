import pytest
from src_0506 import task_func

def test_task_func():
    secret = "secret"
    message = "message"
    expected_result = "098f6bcd4621d373cade4e832627b4f6"
    assert task_func(secret, message) == expected_result