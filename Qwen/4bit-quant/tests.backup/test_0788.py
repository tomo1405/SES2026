import pytest
from src_0788 import task_func
import numpy as np

def test_task_func_equal_length_arrays():
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    assert task_func(array1, array2) == np.sqrt(2)

def test_task_func_single_element_arrays():
    array1 = [0]
    array2 = [0]
    assert task_func(array1, array2) == 0

def test_task_func_zero_distance():
    array1 = [1, 2, 3]
    array2 = [1, 2, 3]
    assert task_func(array1, array2) == 0

def test_task_func_max_distance():
    array1 = [0, 0, 0]
    array2 = [3, 4, 0]
    assert task_func(array1, array2) == 5

def test_task_func_empty_arrays():
    array1 = []
    array2 = []
    assert task_func(array1, array2) == 0

def test_task_func_value_error():
    array1 = [1, 2]
    array2 = [3]
    with pytest.raises(ValueError, match="The input arrays must have the same length."):
        task_func(array1, array2)