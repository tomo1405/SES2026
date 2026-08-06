import codecs
import struct

from src_0546 import task_func


def test_task_func():
    # Test that the function returns a bytes object
    result = task_func()
    assert isinstance(result, bytes)

    # Test that the function returns one of the expected encoded float values
    possible_values = [struct.unpack('!f', bytes.fromhex(key))[0] for key in KEYS]
    possible_encoded_values = [codecs.encode(str(value), 'utf-8') for value in possible_values]
    assert result in possible_encoded_values

    # Test that the function can handle the default KEYS
    result_with_defaults = task_func()
    assert result_with_defaults in possible_encoded_values

    # Test that the function can handle a custom set of KEYS
    custom_keys = ['4E6FC614', '4F5FC614']
    possible_custom_values = [struct.unpack('!f', bytes.fromhex(key))[0] for key in custom_keys]
    possible_custom_encoded_values = [codecs.encode(str(value), 'utf-8') for value in possible_custom_values]
    result_with_custom_keys = task_func(custom_keys)
    assert result_with_custom_keys in possible_custom_encoded_values