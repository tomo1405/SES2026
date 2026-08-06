import pytest
from src_0296 import task_func
import itertools
import statistics

def test_task_func():
    # Test with a simple list and subset size
    elements = [1, 2, 3]
    subset_size = 2
    result = task_func(elements, subset_size)
    expected = {
        'mean': 3.0,
        'median': 3.0,
        'mode': 3
    }
    assert result == expected

    # Test with a larger list and subset size
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    result = task_func(elements, subset_size)
    expected = {
        'mean': 12.0,
        'median': 12.0,
        'mode': 12
    }
    assert result == expected

    # Test with a list where all elements are the same
    elements = [1, 1, 1, 1]
    subset_size = 2
    result = task_func(elements, subset_size)
    expected = {
        'mean': 2.0,
        'median': 2.0,
        'mode': 2
    }
    assert result == expected

    # Test with a list where there is no unique mode
    elements = [1, 2, 2, 3, 3]
    subset_size = 2
    result = task_func(elements, subset_size)
    expected = {
        'mean': 4.0,
        'median': 4.0,
        'mode': 4
    }
    assert result == expected

    # Test with a subset size of 1
    elements = [1, 2, 3]
    subset_size = 1
    result = task_func(elements, subset_size)
    expected = {
        'mean': 2.0,
        'median': 2.0,
        'mode': 1
    }
    assert result == expected

    # Test with an empty list
    elements = []
    subset_size = 0
    result = task_func(elements, subset_size)
    expected = {
        'mean': None,
        'median': None,
        'mode': None
    }
    assert result == expected

    # Test with a list and subset size where combinations are empty
    elements = [1, 2, 3]
    subset_size = 4
    result = task_func(elements, subset_size)
    expected = {
        'mean': None,
        'median': None,
        'mode': None
    }
    assert result == expected