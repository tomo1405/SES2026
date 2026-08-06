import pytest
from src_0296 import task_func

def test_task_func_with_small_list():
    elements = [1, 2, 3]
    subset_size = 2
    result = task_func(elements, subset_size)
    assert result == {
        'mean': 3.0,
        'median': 3.0,
        'mode': 3
    }

def test_task_func_with_larger_list():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    result = task_func(elements, subset_size)
    assert result == {
        'mean': 12.0,
        'median': 12.0,
        'mode': 12
    }

def test_task_func_with_single_element():
    elements = [1]
    subset_size = 1
    result = task_func(elements, subset_size)
    assert result == {
        'mean': 1.0,
        'median': 1.0,
        'mode': 1
    }

def test_task_func_with_no_elements():
    elements = []
    subset_size = 0
    result = task_func(elements, subset_size)
    assert result == {
        'mean': None,
        'median': None,
        'mode': None
    }

def test_task_func_with_duplicate_elements():
    elements = [1, 1, 2, 2, 3]
    subset_size = 2
    result = task_func(elements, subset_size)
    assert result == {
        'mean': 3.0,
        'median': 3.0,
        'mode': 3
    }

def test_task_func_with_non_integer_elements():
    elements = [1.5, 2.5, 3.5]
    subset_size = 2
    result = task_func(elements, subset_size)
    assert result == {
        'mean': 6.0,
        'median': 6.0,
        'mode': 6.0
    }