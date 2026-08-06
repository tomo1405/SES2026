import codecs
import random
import struct
from src_0546 import task_func
import pytest

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def test_task_func():
    hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    encoded_float = codecs.encode(str(float_num), 'utf-8')

    assert task_func(hex_keys=KEYS) == encoded_float

def test_task_func_with_empty_keys():
    with pytest.raises(ValueError):
        task_func(hex_keys=[])

def test_task_func_with_invalid_key():
    with pytest.raises(ValueError):
        task_func(hex_keys=['invalid_key'])