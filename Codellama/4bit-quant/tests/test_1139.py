import pytest
from src_1139 import task_func
import numpy as np

def test_task_func():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sorted_array, combinations = task_func(matrix)
    
    assert np.array_equal(sorted_array, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert len(combinations) == 3
    assert np.array_equal(combinations[0], np.array([1, 2]))
    assert np.array_equal(combinations[1], np.array([1, 3]))
    assert np.array_equal(combinations[2], np.array([2, 3]))