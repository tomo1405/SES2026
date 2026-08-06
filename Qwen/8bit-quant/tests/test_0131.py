import pytest
from src_0131 import task_func

def test_task_func_with_valid_hex_str_and_salt_size():
    hex_str = "68656c6c6f"
    salt_size = 16
    result = task_func(hex_str, salt_size)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

def test_task_func_with_empty_hex_str():
    hex_str = ""
    salt_size = 16
    result = task_func(hex_str, salt_size)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

def test_task_func_with_large_salt_size():
    hex_str = "68656c6c6f"
    salt_size = 1024
    result = task_func(hex_str, salt_size)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

def test_task_func_with_zero_salt_size():
    hex_str = "68656c6c6f"
    salt_size = 0
    result = task_func(hex_str, salt_size)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

def test_task_func_with_special_characters_in_hex_str():
    hex_str = "68656c6c6f21@#"
    salt_size = 16
    result = task_func(hex_str, salt_size)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)