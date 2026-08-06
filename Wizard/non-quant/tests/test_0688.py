python
import numpy as np
import pytest
from scipy.stats import mode

def task_func(list_of_lists):
    merged_list = np.array([item for sublist in list_of_lists for item in sublist])
    mode_value, mode_count = mode(merged_list)
    return mode_value, mode_count

def test_task_func():
    # Test case 1
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = (3, 1)
    assert task_func(list_of_lists) == expected_output

    # Test case 2
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 3, 3]]
    expected_output = (3, 3)
    assert task_func(list_of_lists) == expected_output

    # Test case 3
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3, 4]]
    expected_output = (1, 1)
    assert task_func(list_of_lists) == expected_output