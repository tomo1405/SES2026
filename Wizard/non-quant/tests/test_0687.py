python
import numpy as np
import pytest
from sklearn.preprocessing import OneHotEncoder

def task_func(list_of_lists):
    merged_list = np.array([item for sublist in list_of_lists for item in sublist]).reshape(-1, 1)
    encoder = OneHotEncoder(sparse=False)
    one_hot = encoder.fit_transform(merged_list)
    return one_hot

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    expected_output = np.array([[0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]])
    assert np.array_equal(task_func(list_of_lists), expected_output)