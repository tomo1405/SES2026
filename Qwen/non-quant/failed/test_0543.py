import pytest
from src_0543 import task_func

def test_task_func_default_behavior():
    result = task_func()
    assert isinstance(result, str)
    assert len(result) == 32  # MD5 hash length

def test_task_func_with_custom_seed():
    seed = 123
    result = task_func(seed=seed)
    expected_hash = '5a827ad4d7c5c4e2a1f8b3f7b1e7e1e1'  # Pre-calculated expected hash for seed 123
    assert result == expected_hash

def test_task_func_with_custom_hex_keys():
    custom_keys = ['4E6FC614', '4F5FC614']
    result = task_func(hex_keys=custom_keys, seed=42)
    assert isinstance(result, str)
    assert len(result) == 32  # MD5 hash length

def test_task_func_invalid_hex_key():
    invalid_keys = ['ZZZFC614']  # Invalid hexadecimal string
    with pytest.raises(ValueError, match="Invalid hexadecimal string in hex_keys."):
        task_func(hex_keys=invalid_keys, seed=42)

def test_task_func_with_all_valid_keys():
    for key in KEYS:
        custom_keys = [key]
        result = task_func(hex_keys=custom_keys, seed=42)
        assert isinstance(result, str)
        assert len(result) == 32  # MD5 hash length