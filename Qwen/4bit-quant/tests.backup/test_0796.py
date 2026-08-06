import pytest
from src_0796 import task_func
from collections import deque

def test_task_func_empty_list():
    result = task_func([])
    assert isinstance(result, deque)
    assert len(result) == 0

def test_task_func_single_element():
    result = task_func([42])
    assert isinstance(result, deque)
    assert list(result) == [42]

def test_task_func_multiple_elements():
    result = task_func([1, 2, 3, 4, 5])
    assert isinstance(result, deque)
    assert list(result) == [3, 4, 5, 1, 2]

def test_task_func_non_numeric_elements():
    result = task_func(['a', 'b', 'c'])
    assert isinstance(result, deque)
    assert list(result) == ['a', 'b', 'c']

def test_task_func_mixed_elements():
    result = task_func([1, 'a', 2, 'b', 3])
    assert isinstance(result, deque)
    assert list(result) == ['b', 3, 1, 'a', 2]

def test_task_func_with_negative_numbers():
    result = task_func([-1, -2, -3, 4, 5])
    assert isinstance(result, deque)
    assert list(result) == [4, 5, -1, -2, -3]

def test_task_func_with_floats():
    result = task_func([1.0, 2.0, 3.0])
    assert isinstance(result, deque)
    assert list(result) == [1.0, 2.0, 3.0]