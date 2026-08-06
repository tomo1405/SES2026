import numpy as np
from src_0034 import task_func


def test_task_func_with_positive_numbers():
    list_of_pairs = [(1, 2), (2, 3), (3, 4)]
    expected_result = np.array([24])
    assert np.array_equal(task_func(list_of_pairs), expected_result)

def test_task_func_with_zero():
    list_of_pairs = [(1, 2), (2, 0), (3, 4)]
    expected_result = np.array([0])
    assert np.array_equal(task_func(list_of_pairs), expected_result)

def test_task_func_with_negative_numbers():
    list_of_pairs = [(1, -2), (2, 3), (3, -4)]
    expected_result = np.array([24])
    assert np.array_equal(task_func(list_of_pairs), expected_result)

def test_task_func_with_single_pair():
    list_of_pairs = [(1, 5)]
    expected_result = np.array([5])
    assert np.array_equal(task_func(list_of_pairs), expected_result)

def test_task_func_with_empty_list():
    list_of_pairs = []
    expected_result = np.array([1])  # Since there are no elements, the product is 1 by default.
    assert np.array_equal(task_func(list_of_pairs), expected_result)