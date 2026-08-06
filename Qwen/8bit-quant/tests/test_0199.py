import pytest
from src_0199 import task_func
import numpy as np
import statistics

def test_task_func_empty_data():
    result = task_func([], 5)
    assert np.array_equal(result[0], np.array([]))
    assert result[1] == 0

def test_task_func_single_element():
    result = task_func([10], 5)
    assert np.array_equal(result[0], np.array([]))
    assert result[1] == 0

def test_task_func_all_elements_greater_than_average():
    data = [10, 20, 30, 40, 50]
    result = task_func(data, 5)
    expected_greater_avg = np.array([10, 20, 30, 40, 50])
    expected_num_greater_value = 0
    assert np.array_equal(result[0], expected_greater_avg)
    assert result[1] == expected_num_greater_value

def test_task_func_all_elements_less_than_average():
    data = [5, 4, 3, 2, 1]
    result = task_func(data, 5)
    expected_greater_avg = np.array([])
    expected_num_greater_value = 5
    assert np.array_equal(result[0], expected_greater_avg)
    assert result[1] == expected_num_greater_value

def test_task_func_mixed_elements():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = task_func(data, 5)
    expected_greater_avg = np.array([6, 7, 8, 9, 10])
    expected_num_greater_value = 5
    assert np.array_equal(result[0], expected_greater_avg)
    assert result[1] == expected_num_greater_value

def test_task_func_value_greater_than_all_elements():
    data = [1, 2, 3, 4, 5]
    result = task_func(data, 6)
    expected_greater_avg = np.array([3, 4, 5])
    expected_num_greater_value = 0
    assert np.array_equal(result[0], expected_greater_avg)
    assert result[1] == expected_num_greater_value

def test_task_func_value_less_than_all_elements():
    data = [1, 2, 3, 4, 5]
    result = task_func(data, 0)
    expected_greater_avg = np.array([1, 2, 3, 4, 5])
    expected_num_greater_value = 5
    assert np.array_equal(result[0], expected_greater_avg)
    assert result[1] == expected_num_greater_value