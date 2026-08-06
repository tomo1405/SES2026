import pytest
from src_0006 import task_func

def test_task_func_keys():
    result = task_func()
    assert set(result.keys()) == set(chr(i) for i in range(97, 123))

def test_task_func_values():
    result = task_func()
    for value in result.values():
        assert isinstance(value, float)
        assert value >= 0

def test_task_func_randomness():
    result1 = task_func()
    result2 = task_func()
    assert result1 != result2, "The function should produce different results on each call due to randomness."

def test_task_func_empty_input():
    result = task_func([])
    assert result == {}

def test_task_func_custom_letters():
    custom_letters = ['a', 'b', 'c']
    result = task_func(custom_letters)
    assert set(result.keys()) == set(custom_letters)