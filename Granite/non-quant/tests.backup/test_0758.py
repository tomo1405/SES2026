import pytest
import numpy as np
import datetime
from src_0758 import task_func

def test_task_func():
    arr = np.array(['1.2.3.4', '5.6.7.8', '9.10.11.12'])
    expected_result = np.array(['4.3.2.1', '8.7.6.5', '12.11.10.9'])
    result = task_func(arr)
    assert np.array_equal(result, expected_result)

def test_task_func_with_empty_array():
    arr = np.array([])
    expected_result = np.array([])
    result = task_func(arr)
    assert np.array_equal(result, expected_result)

def test_task_func_with_single_element_array():
    arr = np.array(['1.2.3.4'])
    expected_result = np.array(['4.3.2.1'])
    result = task_func(arr)
    assert np.array_equal(result, expected_result)

def test_task_func_with_invalid_input():
    arr = np.array([1, 2, 3])
    with pytest.raises(TypeError):
        task_func(arr)

def test_task_func_with_unicode_input():
    arr = np.array(['π.π.π.π'])
    with pytest.raises(UnicodeError):
        task_func(arr)