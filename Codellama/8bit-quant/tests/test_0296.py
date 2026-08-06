import pytest
from src_0296 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    expected_result = {
        'mean': 3.0,
        'median': 3.0,
        'mode': 3.0
    }
    assert task_func(elements, subset_size) == expected_result

def test_task_func_with_different_subset_size():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    expected_result = {
        'mean': 2.5,
        'median': 2.5,
        'mode': 2.5
    }
    assert task_func(elements, subset_size) == expected_result

def test_task_func_with_different_elements():
    elements = [1, 2, 3, 4, 5, 6]
    subset_size = 3
    expected_result = {
        'mean': 3.5,
        'median': 3.5,
        'mode': 3.5
    }
    assert task_func(elements, subset_size) == expected_result