import pytest
from src_0543 import task_func

def test_task_func_default_behavior():
    expected_output = 'd41d8cd98f00b204e9800998ecf8427e'  # MD5 hash of "nan"
    assert task_func() == expected_output

def test_task_func_with_custom_seed():
    expected_output = 'd41d8cd98f00b204e9800998ecf8427e'  # MD5 hash of "nan"
    assert task_func(seed=123) == expected_output

def test_task_func_with_custom_hex_keys():
    custom_keys = ['470FC614', '4A0FC614']
    expected_output = 'd41d8cd98f00b204e9800998ecf8427e'  # MD5 hash of "nan"
    assert task_func(hex_keys=custom_keys, seed=123) == expected_output

def test_task_func_invalid_hex_key():
    custom_keys = ['ZZZZZZZZ']  # Invalid hexadecimal string
    with pytest.raises(ValueError, match="Invalid hexadecimal string in hex_keys."):
        task_func(hex_keys=custom_keys, seed=123)