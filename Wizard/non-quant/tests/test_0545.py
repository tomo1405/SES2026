python
import struct
import zlib
import pytest

# Constants
KEY = '470FC614'

def task_func(hex_string=KEY):
    binary_float = struct.pack('!f', int(hex_string, 16))
    compressed_data = zlib.compress(binary_float)
    return compressed_data

def test_task_func():
    assert task_func() == b'\x78\x9c\xcb\x48\xcd\xc9\xc9\x07\x00\x06\x05\x00\x00\x00\x00\x00'