import pytest
from src_0001 import task_func

def test_task_func_default():
    result = task_func()
    assert isinstance(result, float)

def test_task_func_single_element():
    result = task_func([5])
    assert result == 0.0

def test_task_func_two_elements():
    result = task_func([1, 2])
    assert result == 1.0

def test_task_func_three_elements():
    result = task_func([1, 2, 3])
    assert result == 2.0

def test_task_func_four_elements():
    result = task_func([1, 2, 3, 4])
    assert result == 3.0

def test_task_func_negative_numbers():
    result = task_func([-1, -2, -3])
    assert result == 2.0

def test_task_func_mixed_numbers():
    result = task_func([-1, 0, 1])
    assert result == 1.0

def test_task_func_large_numbers():
    result = task_func([10, 20, 30, 40])
    assert result == 30.0

def test_task_func_repeated_numbers():
    result = task_func([1, 1, 1])
    assert result == 0.0