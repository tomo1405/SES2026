import pytest
from src_0199 import task_func
import numpy as np

def test_task_func_empty_data():
    result = task_func([], 5)
    assert np.array_equal(result[0], np.array([]))
    assert result[1] == 0

def test_task_func_all_elements_greater_than_value():
    data = [6, 7, 8, 9]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([6, 7, 8, 9]))
    assert result[1] == 0

def test_task_func_all_elements_less_than_value():
    data = [1, 2, 3, 4]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([]))
    assert result[1] == 4

def test_task_func_mixed_elements():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([6, 7, 8, 9]))
    assert result[1] == 4

def test_task_func_single_element_greater_than_value():
    data = [10]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([10]))
    assert result[1] == 0

def test_task_func_single_element_less_than_value():
    data = [1]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([]))
    assert result[1] == 1

def test_task_func_single_element_equal_to_value():
    data = [5]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([]))
    assert result[1] == 1

def test_task_func_with_negative_numbers():
    data = [-10, -5, 0, 5, 10]
    value = 0
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([5, 10]))
    assert result[1] == 2