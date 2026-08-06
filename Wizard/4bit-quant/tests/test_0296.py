python
import itertools
import statistics
import pytest

def task_func(elements, subset_size):
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    return {
        'mean': statistics.mean(sums),
        'median': statistics.median(sums),
        'mode': statistics.mode(sums)
    }

def test_task_func():
    # Test case 1
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    expected_result = {
        'mean': 3.5,
        'median': 3.5,
        'mode': 3
    }
    assert task_func(elements, subset_size) == expected_result

    # Test case 2
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    expected_result = {
        'mean': 3.5,
        'median': 3.5,
        'mode': 3
    }
    assert task_func(elements, subset_size) == expected_result

    # Test case 3
    elements = [1, 2, 3, 4, 5]
    subset_size = 4
    expected_result = {
        'mean': 3.5,
        'median': 3.5,
        'mode': 3
    }
    assert task_func(elements, subset_size) == expected_result

    # Test case 4
    elements = [1, 2, 3, 4, 5]
    subset_size = 5
    expected_result = {
        'mean': 3.5,
        'median': 3.5,
        'mode': 3
    }
    assert task_func(elements, subset_size) == expected_result

    # Test case 5
    elements = [1, 2, 3, 4, 5]
    subset_size = 6
    expected_result = {
        'mean': 3.5,
        'median': 3.5,
        'mode': 3
    }
    assert task_func(elements, subset_size) == expected_result