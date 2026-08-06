import struct
import zlib
from src_0545 import task_func
import pytest

# Constants
KEY = '470FC614'
BINARY_FLOAT = struct.pack('!f', int(KEY, 16))
COMPRESSED_DATA = zlib.compress(BINARY_FLOAT)

def test_task_func():
    assert task_func(hex_string=KEY) == COMPRESSED_DATA

def test_task_func_with_default_argument():
    assert task_func() == COMPRESSED_DATA

def test_task_func_with_invalid_hex_string():
    with pytest.raises(ValueError):
        task_func(hex_string='invalid_hex_string')