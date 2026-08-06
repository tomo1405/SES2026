python
import pytest
from src_0534 import task_func

def test_task_func():
    num = '1234567890'
    from_base = 10
    to_base = 62
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    base64_encoded, salt = task_func(num, from_base, to_base, alphabet)

    assert isinstance(base64_encoded, str)
    assert isinstance(salt, str)
    assert len(salt) == 32
    assert len(base64_encoded) == 22