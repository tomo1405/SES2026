import pytest
from src_0296 import task_func
import statistics

def test_task_func_with_even_elements():
    elements = [1, 2, 3, 4]
    subset_size = 2
    result = task_func(elements, subset_size)
    expected_sums = [3, 4, 5, 5, 6, 7]
    assert result['mean'] == statistics.mean(expected_sums)
    assert result['median'] == statistics.median(expected_sums)
    assert result['mode'] == statistics.mode(expected_sums)

def test_task_func_with_odd_elements():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    result = task_func(elements, subset_size)
    expected_sums = [6, 7, 8, 8, 9, 9, 10, 10, 11, 12]
    assert result['mean'] == statistics.mean(expected_sums)
    assert result['median'] == statistics.median(expected_sums)
    assert result['mode'] == statistics.mode(expected_sums)

def test_task_func_single_element_subset():
    elements = [1, 2, 3, 4]
    subset_size = 1
    result = task_func(elements, subset_size)
    expected_sums = [1, 2, 3, 4]
    assert result['mean'] == statistics.mean(expected_sums)
    assert result['median'] == statistics.median(expected_sums)
    assert result['mode'] == statistics.mode(expected_sums)

def test_task_func_empty_list():
    elements = []
    subset_size = 0
    result = task_func(elements, subset_size)
    expected_sums = [0]  # Sum of an empty subset is 0
    assert result['mean'] == statistics.mean(expected_sums)
    assert result['median'] == statistics.median(expected_sums)
    assert result['mode'] == statistics.mode(expected_sums)

def test_task_func_single_element_list():
    elements = [1]
    subset_size = 1
    result = task_func(elements, subset_size)
    expected_sums = [1]
    assert result['mean'] == statistics.mean(expected_sums)
    assert result['median'] == statistics.median(expected_sums)
    assert result['mode'] == statistics.mode(expected_sums)

def test_task_func_no_combinations():
    elements = [1, 2, 3]
    subset_size = 4
    with pytest.raises(ValueError):
        task_func(elements, subset_size)