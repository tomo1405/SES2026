import struct
import random
from src_0740 import task_func
import pytest

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def test_task_func_with_random_key():
    hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    expected_result = round(float_num, 2)
    result = task_func(hex_key)
    assert result == expected_result

def test_task_func_with_specific_key():
    hex_key = '4A0FC614'
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    expected_result = round(float_num, 2)
    result = task_func(hex_key)
    assert result == expected_result

def test_task_func_with_invalid_key():
    hex_key = 'invalid_key'
    with pytest.raises(ValueError):
        task_func(hex_key)