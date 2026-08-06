import base64
import binascii

import pytest
from src_0131 import task_func


def test_task_func():
    hex_str = "68656c6c6f"
    salt_size = 16

    result = task_func(hex_str, salt_size)
    assert isinstance(result, tuple)
    assert len(result) == 2

    salt_base64, hash_value = result
    assert isinstance(salt_base64, str)
    assert isinstance(hash_value, str)

    # Decode the base64 salt back to bytes and check its length
    salt_bytes = base64.b64decode(salt_base64)
    assert len(salt_bytes) == salt_size

    # Check that the hash value is a valid SHA-256 hash
    assert len(hash_value) == 64  # SHA-256 hash length in hexadecimal

def test_task_func_with_different_salt_size():
    hex_str = "68656c6c6f"
    salt_size = 8

    result = task_func(hex_str, salt_size)
    assert isinstance(result, tuple)
    assert len(result) == 2

    salt_base64, hash_value = result
    assert isinstance(salt_base64, str)
    assert isinstance(hash_value, str)

    # Decode the base64 salt back to bytes and check its length
    salt_bytes = base64.b64decode(salt_base64)
    assert len(salt_bytes) == salt_size

    # Check that the hash value is a valid SHA-256 hash
    assert len(hash_value) == 64  # SHA-256 hash length in hexadecimal

def test_task_func_with_empty_hex_str():
    hex_str = ""
    salt_size = 16

    result = task_func(hex_str, salt_size)
    assert isinstance(result, tuple)
    assert len(result) == 2

    salt_base64, hash_value = result
    assert isinstance(salt_base64, str)
    assert isinstance(hash_value, str)

    # Decode the base64 salt back to bytes and check its length
    salt_bytes = base64.b64decode(salt_base64)
    assert len(salt_bytes) == salt_size

    # Check that the hash value is a valid SHA-256 hash
    assert len(hash_value) == 64  # SHA-256 hash length in hexadecimal

def test_task_func_with_invalid_hex_str():
    hex_str = "68656c6l"  # 'l' is invalid in hex
    salt_size = 16

    with pytest.raises(binascii.Error):
        task_func(hex_str, salt_size)