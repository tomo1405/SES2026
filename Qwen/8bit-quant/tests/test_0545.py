import struct
import zlib

import pytest
from src_0545 import task_func


def test_task_func_default():
    # Test with the default KEY
    expected_hex_string = '470FC614'
    expected_binary_float = struct.pack('!f', int(expected_hex_string, 16))
    expected_compressed_data = zlib.compress(expected_binary_float)
    assert task_func() == expected_compressed_data

def test_task_func_custom_key():
    # Test with a custom key
    custom_key = '12345678'
    expected_binary_float = struct.pack('!f', int(custom_key, 16))
    expected_compressed_data = zlib.compress(expected_binary_float)
    assert task_func(custom_key) == expected_compressed_data

def test_task_func_invalid_key():
    # Test with an invalid key that cannot be converted to an integer
    invalid_key = 'GHIJKL'
    with pytest.raises(ValueError):
        task_func(invalid_key)

def test_task_func_empty_key():
    # Test with an empty key
    with pytest.raises(ValueError):
        task_func('')