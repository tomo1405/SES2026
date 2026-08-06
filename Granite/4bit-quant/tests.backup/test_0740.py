import struct
import random
from src_0740 import task_func

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def test_task_func():
    hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    expected_result = round(float_num, 2)
    actual_result = task_func(hex_key)
    assert actual_result == expected_result, "task_func returned an incorrect result"

def test_task_func_with_none_input():
    expected_result = task_func()
    actual_result = task_func(None)
    assert actual_result == expected_result, "task_func returned an incorrect result when called with None input"