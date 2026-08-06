import pytest
from src_0543 import task_func

def test_task_func_default_behavior():
    expected_hash = 'b10a8db164e0754105b7a99be72e3fe5'
    assert task_func() == expected_hash

def test_task_func_with_custom_seed():
    custom_seed = 123
    expected_hash = 'c9b1d7b1e6b8f1b1e6b8f1b1e6b8f1b1'
    assert task_func(seed=custom_seed) == expected_hash

def test_task_func_with_custom_keys():
    custom_keys = ['4A0FC614', '4B9FC614']
    expected_hash = 'b10a8db164e0754105b7a99be72e3fe5'
    assert task_func(hex_keys=custom_keys) == expected_hash

def test_task_func_invalid_hex_key():
    invalid_keys = ['ZZZZZZZZ']
    with pytest.raises(ValueError, match="Invalid hexadecimal string in hex_keys."):
        task_func(hex_keys=invalid_keys)