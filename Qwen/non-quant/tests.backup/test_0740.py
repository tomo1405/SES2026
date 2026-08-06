import pytest
from src_0740 import task_func

def test_task_func_with_default_key():
    # Test with default key selection
    result = task_func()
    assert isinstance(result, float)

def test_task_func_with_specific_key():
    # Test with a specific key
    hex_key = '470FC614'
    expected_float = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    expected_rounded = round(expected_float, 2)
    result = task_func(hex_key)
    assert result == expected_rounded

def test_task_func_with_all_keys():
    # Test with all possible keys
    for hex_key in KEYS:
        expected_float = struct.unpack('!f', bytes.fromhex(hex_key))[0]
        expected_rounded = round(expected_float, 2)
        result = task_func(hex_key)
        assert result == expected_rounded

def test_task_func_random_key():
    # Test with random key selection
    result = task_func(None)
    assert isinstance(result, float)