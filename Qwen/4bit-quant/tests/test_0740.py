import struct

import pytest
from src_0740 import task_func


def test_task_func_with_valid_hex_key():
    # Test with a valid hex key
    hex_key = '470FC614'
    result = task_func(hex_key)
    assert isinstance(result, float), "The result should be a float"
    # The expected value is calculated based on the struct.unpack and rounding
    expected_value = round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2)
    assert result == expected_value, f"Expected {expected_value}, got {result}"

def test_task_func_with_no_hex_key():
    # Test with no hex key provided, should use a random choice from KEYS
    result = task_func()
    assert isinstance(result, float), "The result should be a float"
    # Check if the result is one of the possible values
    expected_values = [round(struct.unpack('!f', bytes.fromhex(key))[0], 2) for key in KEYS]
    assert result in expected_values, f"Result {result} should be one of {expected_values}"

def test_task_func_with_invalid_hex_key():
    # Test with an invalid hex key
    invalid_hex_key = 'INVALID_KEY'
    with pytest.raises(ValueError):
        task_func(invalid_hex_key)

def test_task_func_with_short_hex_key():
    # Test with a short hex key
    short_hex_key = '1234'
    with pytest.raises(ValueError):
        task_func(short_hex_key)

def test_task_func_with_long_hex_key():
    # Test with a long hex key
    long_hex_key = '123456789ABCDEF0'
    with pytest.raises(ValueError):
        task_func(long_hex_key)