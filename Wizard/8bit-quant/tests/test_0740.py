python
import struct
import random
import pytest

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_key=None):
    if hex_key is None:
        hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    rounded_float = round(float_num, 2)
    return rounded_float

def test_task_func():
    assert task_func() == 470.86
    assert task_func('4A0FC614') == 490.86
    assert task_func('4B9FC614') == 489.86
    assert task_func('4C8FC614') == 488.86
    assert task_func('4D7FC614') == 487.86