import numpy as np
from src_0758 import task_func


def test_task_func_with_empty_array():
    arr = np.array([])
    result = task_func(arr)
    assert np.array_equal(result, np.array([]))

def test_task_func_with_single_element():
    arr = np.array(['1.2.3'])
    result = task_func(arr)
    assert np.array_equal(result, np.array(['3.2.1']))

def test_task_func_with_multiple_elements():
    arr = np.array(['1.2.3', '4.5.6', '7.8.9'])
    result = task_func(arr)
    assert np.array_equal(result, np.array(['3.2.1', '6.5.4', '9.8.7']))

def test_task_func_with_single_digit_elements():
    arr = np.array(['1', '2', '3'])
    result = task_func(arr)
    assert np.array_equal(result, np.array(['1', '2', '3']))

def test_task_func_with_complex_elements():
    arr = np.array(['1.2.3.4', '5.6.7.8.9'])
    result = task_func(arr)
    assert np.array_equal(result, np.array(['4.3.2.1', '9.8.7.6.5']))

def test_task_func_with_mixed_elements():
    arr = np.array(['1.2.3', '4', '5.6.7.8'])
    result = task_func(arr)
    assert np.array_equal(result, np.array(['3.2.1', '4', '8.7.6.5']))