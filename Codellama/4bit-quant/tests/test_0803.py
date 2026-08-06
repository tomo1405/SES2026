import itertools

import numpy as np
import pytest
from src_0803 import task_func


def test_task_func():
    # Test with valid input
    dimension = 3
    seed = 42
    expected_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_combinations = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    
    matrix, flat_list = task_func(dimension, seed)
    
    assert np.array_equal(matrix, expected_matrix)
    assert flat_list == expected_flat_list
    assert list(itertools.combinations(flat_list, 2)) == expected_combinations
    
    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(0)