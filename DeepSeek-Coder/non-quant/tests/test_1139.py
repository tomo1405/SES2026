import pytest
from src_1139 import task_func
import numpy as np
import itertools

def test_task_func():
    # Test case 1: Basic test
    matrix = np.array([[1, 2], [3, 4]])
    sorted_array, combinations = task_func(matrix)
    assert sorted_array == [1, 2, 3, 4]
    assert combinations == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

    # Add more test cases as needed

# Add more test cases as needed