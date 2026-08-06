import pytest
from src_1139 import task_func
import numpy as np
import itertools

def test_task_func():
    matrix = np.array([[1, 4, 2], [3, 2, 5]])
    expected_sorted_array = np.array([1, 2, 2, 3, 4, 5])
    expected_combinations = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    
    sorted_array, combinations = task_func(matrix)
    
    assert np.array_equal(sorted_array, expected_sorted_array)
    assert combinations == expected_combinations