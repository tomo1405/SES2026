python
import pytest
from src_0534 import task_func

def test_task_func():
    num = '123456789'
    from_base = 10
    to_base = 62
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result, salt = task_func(num, from_base, to_base, alphabet)

    assert isinstance(result, str)
    assert isinstance(salt, str)
    assert len(salt) == 32
    assert len(result) == 22