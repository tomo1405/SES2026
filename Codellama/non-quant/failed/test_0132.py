import pytest
from src_0132 import task_func

def test_task_func():
    hex_str = "0123456789abcdef"
    salt_size = 16
    expected_salt = "0123456789abcdef"
    expected_hash = "0123456789abcdef"

    salt, hash_value = task_func(hex_str, salt_size)

    assert salt == expected_salt
    assert hash_value == expected_hash