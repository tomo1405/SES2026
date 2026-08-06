import pytest
from src_0546 import task_func

def test_task_func():
    hex_keys = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
    for hex_key in hex_keys:
        float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
        encoded_float = codecs.encode(str(float_num), 'utf-8')
        assert task_func(hex_keys=[hex_key]) == encoded_float