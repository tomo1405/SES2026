import pytest
from src_0788 import task_func
import numpy as np

def test_task_func_equal_length_arrays():
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    assert task_func(array1, array2) == np.sqrt(2)

def test_task_func_single_element_arrays():
    array1 = np.array([1])
    array2 = np.array([2])
    assert task_func(array1, array2) == 0

def test_task_func_empty_arrays():
    array1 = np.array([])
    array2 = np.array([])
    assert task_func(array1, array2) == 0

def test_task_func_different_length_arrays():
    array1 = np.array([1, 2])
    array2 = np.array([3])
    with pytest.raises(ValueError, match="The input arrays must have the same length."):
        task_func(array1, array2)

def test_task_func_large_numbers():
    array1 = np.array([1e9, 2e9, 3e9])
    array2 = np.array([4e9, 5e9, 6e9])
    assert task_func(array1, array2) == np.sqrt(2)

def test_task_func_negative_numbers():
    array1 = np.array([-1, -2, -3])
    array2 = np.array([-4, -5, -6])
    assert task_func(array1, array2) == np.sqrt(2)

def test_task_func_mixed_positive_negative_numbers():
    array1 = np.array([-1, 2, -3])
    array2 = np.array([4, -5, 6])
    assert task_func(array1, array2) == np.sqrt(2)