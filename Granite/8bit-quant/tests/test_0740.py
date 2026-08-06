import random
import struct

import pytest
from src_0740 import task_func

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def test_task_func_with_hex_key():
    hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    rounded_float = round(float_num, 2)
    assert task_func(hex_key) == rounded_float

def test_task_func_without_hex_key():
    hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    rounded_float = round(float_num, 2)
    assert task_func() == rounded_float

def test_task_func_with_invalid_hex_key():
    hex_key = 'invalid_key'
    with pytest.raises(ValueError):
        task_func(hex_key)