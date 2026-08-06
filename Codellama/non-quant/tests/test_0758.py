import pytest
from src_0758 import task_func
import numpy as np
import datetime

def test_task_func():
    arr = np.array(['1.2.3', '4.5.6', '7.8.9'])
    expected = np.array(['3.2.1', '6.5.4', '9.8.7'])
    assert np.array_equal(task_func(arr), expected)

def test_task_func_with_invalid_input():
    arr = np.array(['1.2.3', '4.5.6', '7.8.9', 'a.b.c'])
    with pytest.raises(ValueError):
        task_func(arr)

def test_task_func_with_empty_input():
    arr = np.array([])
    expected = np.array([])
    assert np.array_equal(task_func(arr), expected)

def test_task_func_with_single_element_input():
    arr = np.array(['1.2.3'])
    expected = np.array(['3.2.1'])
    assert np.array_equal(task_func(arr), expected)

def test_task_func_with_datetime_input():
    arr = np.array([datetime.datetime.now()])
    with pytest.raises(TypeError):
        task_func(arr)

def test_task_func_with_numpy_array_input():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        task_func(arr)