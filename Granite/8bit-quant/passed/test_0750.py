import pytest
from src_0750 import task_func
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def test_task_func():
    myList = [1, 2, 3, 4, 5]
    expected_output = np.array([0., 0.2, 0.4, 0.6, 0.8]).reshape(-1, 1)
    actual_output = task_func(myList)
    assert np.array_equal(actual_output, expected_output)

def test_task_func_with_negative_values():
    myList = [-1, -2, -3, -4, -5]
    expected_output = np.array([0., 0., 0., 0., 0.]).reshape(-1, 1)
    actual_output = task_func(myList)
    assert np.array_equal(actual_output, expected_output)

def test_task_func_with_zero_values():
    myList = [0, 0, 0, 0, 0]
    expected_output = np.array([0.5, 0.5, 0.5, 0.5, 0.5]).reshape(-1, 1)
    actual_output = task_func(myList)
    assert np.array_equal(actual_output, expected_output)

def test_task_func_with_one_value():
    myList = [10]
    expected_output = np.array([1.]).reshape(-1, 1)
    actual_output = task_func(myList)
    assert np.array_equal(actual_output, expected_output)

def test_task_func_with_empty_list():
    myList = []
    with pytest.raises(ValueError):
        task_func(myList)