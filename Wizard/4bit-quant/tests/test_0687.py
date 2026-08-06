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
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    expected_one_hot = np.array([[0., 1., 0., 0., 1., 0., 0., 1., 0.],
                                  [1., 0., 0., 0., 0., 1., 0., 0., 1.]])
    one_hot = task_func(list_of_lists)
    assert np.array_equal(one_hot, expected_one_hot)

    # Test case 2
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_one_hot = np.array([[0., 1., 0., 0., 1., 0., 0., 1., 0.],
                                  [1., 0., 0., 0., 0., 1., 0., 0., 1.],
                                  [0., 0., 1., 0., 0., 0., 1., 0., 0.]])
    one_hot = task_func(list_of_lists)
    assert np.array_equal(one_hot, expected_one_hot)

    # Test case 3
    list_of_lists = []
    expected_one_hot = np.array([])
    one_hot = task_func(list_of_lists)
    assert np.array_equal(one_hot, expected_one_hot)

    # Test case 4
    list_of_lists = [[], [], []]
    expected_one_hot = np.array([])
    one_hot = task_func(list_of_lists)
    assert np.array_equal(one_hot, expected_one_hot)

    # Test case 5
    list_of_lists = [[1, 2, 3], [], [4, 5, 6]]
    expected_one_hot = np.array([[0., 1., 0., 0., 1., 0., 0., 1., 0.],
                                  [0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                  [1., 0., 0., 0., 0., 1., 0., 0., 1.]])
    one_hot = task_func(list_of_lists)
    assert np.array_equal(one_hot, expected_one_hot)