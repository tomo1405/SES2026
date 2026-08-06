python
import codecs
import random
import struct

from src_0546 import task_func

def test_task_func():
    KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
    hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    encoded_float = codecs.encode(str(float_num), 'utf-8')

    assert task_func(KEYS) == encoded_float