python
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import pytest

def task_func(list_of_lists):
    merged_list = np.array([item for sublist in list_of_lists for item in sublist]).reshape(-1, 1)
    encoder = OneHotEncoder(sparse=False)
    one_hot = encoder.fit_transform(merged_list)
    return one_hot

def test_task_func():
    # Test case 1
    input_list = [[1, 2, 3], [4, 5, 6]]
    expected_output = np.array([[0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]])
    assert np.array_equal(task_func(input_list), expected_output)

    # Test case 2
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = np.array([[0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]])
    assert np.array_equal(task_func(input_list), expected_output)

    # Test case 3
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    expected_output = np.array([[0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0]])
    assert np.array_equal(task_func(input_list), expected_output)