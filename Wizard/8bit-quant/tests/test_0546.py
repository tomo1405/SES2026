python
import codecs
import random
import struct
import pytest

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS):
    hex_key = random.choice(hex_keys)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    encoded_float = codecs.encode(str(float_num), 'utf-8')

    return encoded_float

def test_task_func():
    assert task_func() == b'3.1415927410125732'