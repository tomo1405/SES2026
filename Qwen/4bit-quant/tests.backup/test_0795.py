import pytest
from src_0795 import task_func

def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) == length

def test_task_func_characters():
    result = task_func(10)
    valid_chars = string.ascii_lowercase + "(){}[]"
    assert all(char in valid_chars for char in result)

def test_task_func_randomness():
    random_seed = 42
    result1 = task_func(10, random_seed)
    result2 = task_func(10, random_seed)
    assert result1 == result2

def test_task_func_with_zero_length():
    result = task_func(0)
    assert result == ""

def test_task_func_with_large_length():
    length = 100
    result = task_func(length)
    assert len(result) == length
    valid_chars = string.ascii_lowercase + "(){}[]"
    assert all(char in valid_chars for char in result)