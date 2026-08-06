import pytest
from src_0796 import task_func
from collections import deque

def test_task_func_empty_list():
    result = task_func([])
    assert result == deque()

def test_task_func_single_element():
    result = task_func([1])
    assert result == deque([1])

def test_task_func_multiple_elements():
    result = task_func([1, 2, 3, 4, 5])
    assert result == deque([3, 4, 5, 1, 2])

def test_task_func_with_non_numeric_elements():
    result = task_func([1, 'a', 3, 'b', 5])
    assert result == deque([3, 'b', 5, 1, 'a'])

def test_task_func_all_numeric_elements():
    result = task_func([1, 2, 3, 4, 5])
    assert result == deque([3, 4, 5, 1, 2])

def test_task_func_negative_numbers():
    result = task_func([-1, -2, -3, -4, -5])
    assert result == deque([-3, -4, -5, -1, -2])

def test_task_func_mixed_positive_and_negative_numbers():
    result = task_func([1, -2, 3, -4, 5])
    assert result == deque([3, -4, 5, 1, -2])

def test_task_func_float_numbers():
    result = task_func([1.0, 2.5, 3.3, 4.8, 5.1])
    assert result == deque([3.3, 4.8, 5.1, 1.0, 2.5])

def test_task_func_mixed_int_and_float():
    result = task_func([1, 2.5, 3, 4.8, 5])
    assert result == deque([3, 4.8, 5, 1, 2.5])