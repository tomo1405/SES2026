import pytest
from src_0788 import task_func
import numpy as np

def test_task_func_equal_arrays():
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    assert task_func(array1, array2) == np.linalg.norm(np.array([1, 2, 3]) - np.array([4, 5, 6]))

def test_task_func_single_element():
    array1 = [1]
    array2 = [2]
    assert task_func(array1, array2) == 1

def test_task_func_empty_arrays():
    array1 = []
    array2 = []
    assert task_func(array1, array2) == 0

def test_task_func_identical_arrays():
    array1 = [1, 1, 1]
    array2 = [1, 1, 1]
    assert task_func(array1, array2) == 0

def test_task_func_different_lengths():
    array1 = [1, 2]
    array2 = [3, 4, 5]
    with pytest.raises(ValueError, match="The input arrays must have the same length."):
        task_func(array1, array2)

def test_task_func_2d_arrays():
    array1 = [[1, 2], [3, 4]]
    array2 = [[5, 6], [7, 8]]
    max_distance = max(np.linalg.norm(np.array([1, 2]) - np.array([5, 6])),
                      np.linalg.norm(np.array([1, 2]) - np.array([7, 8])),
                      np.linalg.norm(np.array([3, 4]) - np.array([5, 6])),
                      np.linalg.norm(np.array([3, 4]) - np.array([7, 8])))
    assert task_func(array1, array2) == max_distance

def test_task_func_negative_numbers():
    array1 = [-1, -2, -3]
    array2 = [-4, -5, -6]
    assert task_func(array1, array2) == np.linalg.norm(np.array([-1, -2, -3]) - np.array([-4, -5, -6]))