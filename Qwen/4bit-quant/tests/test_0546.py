import codecs
import struct

from src_0546 import task_func


def test_task_func():
    # Test that the function returns a byte string
    result = task_func()
    assert isinstance(result, bytes)

    # Test that the function returns one of the expected byte strings
    expected_keys = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
    for key in expected_keys:
        float_num = struct.unpack('!f', bytes.fromhex(key))[0]
        encoded_float = codecs.encode(str(float_num), 'utf-8')
        assert result == encoded_float

    # Test that the function returns different results with different random choices
    results = set()
    for _ in range(10):
        results.add(task_func())
    assert len(results) > 1

def test_task_func_with_custom_keys():
    custom_keys = ['4E6FC614', '4F5FC614']
    result = task_func(custom_keys)
    assert isinstance(result, bytes)

    # Test that the function returns one of the expected byte strings from custom keys
    for key in custom_keys:
        float_num = struct.unpack('!f', bytes.fromhex(key))[0]
        encoded_float = codecs.encode(str(float_num), 'utf-8')
        assert result == encoded_float