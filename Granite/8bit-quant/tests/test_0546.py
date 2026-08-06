import codecs
import random
import struct
from src_0546 import task_func
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def test_task_func_with_default_keys():
    hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    encoded_float = codecs.encode(str(float_num), 'utf-8')
    assert task_func() == encoded_float

def test_task_func_with_custom_keys():
    custom_keys = ['12345678', '87654321']
    hex_key = random.choice(custom_keys)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    encoded_float = codecs.encode(str(float_num), 'utf-8')
    assert task_func(custom_keys) == encoded_float

def test_task_func_with_empty_keys():
    assert task_func([]) is None