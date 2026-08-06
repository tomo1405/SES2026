import struct
import zlib
from src_0545 import task_func
import pytest

# Constants
KEY = '470FC614'

def test_task_func():
    hex_string = KEY
    binary_float = struct.pack('!f', int(hex_string, 16))
    compressed_data = zlib.compress(binary_float)
    expected_result = task_func(hex_string)
    assert expected_result == compressed_data

def test_task_func_with_invalid_hex_string():
    hex_string = 'invalid_hex_string'
    with pytest.raises(ValueError):
        task_func(hex_string)