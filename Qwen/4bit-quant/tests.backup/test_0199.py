import pytest
from src_0199 import task_func
import numpy as np
import statistics
import matplotlib.pyplot as plt

# Mocking the matplotlib show function to prevent GUI display during tests
plt.show = lambda: None

def test_task_func_empty_data():
    data = []
    value = 5
    result = task_func(data, value)
    assert isinstance(result[0], np.ndarray)
    assert result[0].size == 0
    assert result[1] == 0

def test_task_func_no_elements_greater_than_average():
    data = [1, 2, 3, 4, 5]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([]))
    assert result[1] == 0

def test_task_func_all_elements_greater_than_average():
    data = [6, 7, 8, 9, 10]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([6, 7, 8, 9, 10]))
    assert result[1] == 0

def test_task_func_some_elements_greater_than_average():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    value = 5
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([6, 7, 8, 9, 10]))
    assert result[1] == 5

def test_task_func_value_greater_than_all_elements():
    data = [1, 2, 3, 4, 5]
    value = 10
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([]))
    assert result[1] == 5

def test_task_func_value_less_than_all_elements():
    data = [1, 2, 3, 4, 5]
    value = 0
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([1, 2, 3, 4, 5]))
    assert result[1] == 0

def test_task_func_value_between_elements():
    data = [1, 2, 3, 4, 5]
    value = 3
    result = task_func(data, value)
    assert np.array_equal(result[0], np.array([4, 5]))
    assert result[1] == 2