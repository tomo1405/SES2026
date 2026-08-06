import numpy as np
from sklearn.preprocessing import OneHotEncoder
from src_0687 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = OneHotEncoder(sparse=False).fit_transform(np.array(list_of_lists).reshape(-1, 1))
    actual_output = task_func(list_of_lists)
    np.testing.assert_array_equal(actual_output, expected_output)

def test_task_func_with_empty_list():
    list_of_lists = [[]]
    expected_output = OneHotEncoder(sparse=False).fit_transform(np.array(list_of_lists).reshape(-1, 1))
    actual_output = task_func(list_of_lists)
    np.testing.assert_array_equal(actual_output, expected_output)

def test_task_func_with_list_of_strings():
    list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f']]
    expected_output = OneHotEncoder(sparse=False).fit_transform(np.array(list_of_lists).reshape(-1, 1))
    actual_output = task_func(list_of_lists)
    np.testing.assert_array_equal(actual_output, expected_output)