import pytest
from src_0796 import task_func
from collections import deque

def test_task_func_empty_list():
    assert task_func([]) == deque()

def test_task_func_single_element():
    assert task_func([1]) == deque([1])

def test_task_func_multiple_elements():
    result = task_func([1, 2, 3, 4])
    assert result == deque([2, 3, 4, 1])

def test_task_func_with_non_numeric_elements():
    result = task_func([1, 'a', 3.5, 'b'])
    assert result == deque(['a', 3.5, 'b', 1])

def test_task_func_with_negative_numbers():
    result = task_func([-1, -2, -3, -4])
    assert result == deque([-2, -3, -4, -1])

def test_task_func_with_mixed_types():
    result = task_func([1, 2, 3, 'a', 4.5, 'b'])
    assert result == deque([2, 3, 'a', 4.5, 'b', 1])

def test_task_func_with_no_numeric_elements():
    result = task_func(['a', 'b', 'c'])
    assert result == deque(['b', 'c', 'a'])

def test_task_func_with_all_numeric_elements():
    result = task_func([1, 2, 3, 4])
    assert result == deque([2, 3, 4, 1])
    # The print statement will be tested indirectly by capturing stdout
    # However, since we are not asserting the printed value, this is just a placeholder for demonstration.