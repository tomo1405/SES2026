python
import binascii
import string
import random
import pytest

def task_func(length):
    HEX_CHARS = string.hexdigits.lower()
    hex_string = "".join(random.choice(HEX_CHARS) for _ in range(length))
    return binascii.unhexlify(hex_string).decode("utf-8", "ignore")

def test_task_func():
    assert task_func(10) == "0123456789"
    assert task_func(20) == "0123456789abcdef0123456789"
    assert task_func(30) == "0123456789abcdef0123456789abcdef0123456789"
    assert task_func(40) == "0123456789abcdef0123456789abcdef0123456789abcdef0123456789"
    assert task_func(50) == "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"