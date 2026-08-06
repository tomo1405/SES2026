import pytest
from src_0796 import task_func
from collections import deque
import math

def test_task_func_empty_list():
    result = task_func([])
    assert isinstance(result, deque)
    assert len(result) == 0

def test_task_func_non_empty_list():
    result = task_func([1, 2, 3, 4, 5])
    assert isinstance(result, deque)
    assert len(result) == 5
    assert result == deque([4, 5, 1, 2, 3])

def test_task_func_with_negative_numbers():
    result = task_func([-1, -2, -3, -4, -5])
    assert isinstance(result, deque)
    assert len(result) == 5
    assert result == deque([-3, -2, -1, -5, -4])

def test_task_func_with_mixed_numbers():
    result = task_func([1, 2, 3, 'a', 4, 'b', 5])
    assert isinstance(result, deque)
    assert len(result) == 6
    assert result == deque([4, 5, 1, 2, 3, 'a'])

def test_task_func_with_zero_sum():
    result = task_func([0, 0, 0])
    assert isinstance(result, deque)
    assert len(result) == 3
    assert result == deque([0, 0, 0])

def test_task_func_with_large_numbers():
    result = task_func([10**10, 2**32, 3**4])
    assert isinstance(result, deque)
    assert len(result) == 3
    assert result == deque([3**4, 10**10, 2**32])