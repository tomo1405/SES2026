python
import base64
import binascii
import os
import hashlib
import pytest

def task_func(hex_str, salt_size):
    salt = os.urandom(salt_size)
    data = binascii.unhexlify(hex_str.replace('\\x', ''))
    salted_data = salt + data
    hash_value = hashlib.sha256(salted_data).hexdigest()

    return (base64.b64encode(salt).decode('utf-8'), hash_value)

def test_task_func():
    hex_str = '48656c6c6f20776f726c64'
    salt_size = 16
    expected_result = ('c2VjcmV0', 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9')
    assert task_func(hex_str, salt_size) == expected_result