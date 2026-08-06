import base64
import binascii
import os
import hashlib
import pytest

from src_0131 import task_func

def test_task_func():
    hex_str = '48656c6c6f'
    salt_size = 16
    salt, hash_value = task_func(hex_str, salt_size)
    assert isinstance(salt, str)
    assert len(salt) == salt_size * 2
    assert isinstance(hash_value, str)
    assert len(hash_value) == 64
    assert hash_value == hashlib.sha256(salt.encode('utf-8') + binascii.unhexlify(hex_str.replace('\\x', '')) .hexdigest()