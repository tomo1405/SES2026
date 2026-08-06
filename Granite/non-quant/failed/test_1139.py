import pytest
from src_1139 import task_func

def test_task_func():
    matrix = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    expected_sorted_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    expected_combinations = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (3, 6), (4, 5), (4, 7), (5, 7), (5, 8), (6, 7), (6, 9), (7, 8), (7, 9), (8, 9)]
    
    sorted_array, combinations = task_func(matrix)
    
    assert np.array_equal(sorted_array, expected_sorted_array)
    assert combinations == expected_combinations