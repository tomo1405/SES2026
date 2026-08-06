import pytest
from src_0992 import task_func

def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) == length // 2

def test_task_func_characters():
    length = 10
    result = task_func(length)
    assert all(c in string.printable for c in result)

def test_task_func_empty_string():
    length = 0
    result = task_func(length)
    assert result == ""

def test_task_func_single_character():
    length = 1
    result = task_func(length)
    assert len(result) == 0

def test_task_func_odd_length():
    length = 9
    result = task_func(length)
    assert len(result) == length // 2

def test_task_func_randomness():
    length = 20
    result1 = task_func(length)
    result2 = task_func(length)
    assert result1 != result2