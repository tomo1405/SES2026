import numpy as np
from src_0034 import task_func


def test_task_func():
    list_of_pairs = [(1, 2), (3, 4), (5, 6)]
    expected_result = np.array([120])
    assert np.array_equal(task_func(list_of_pairs), expected_result)


def test_task_func_empty_list():
    list_of_pairs = []
    expected_result = np.array([])
    assert np.array_equal(task_func(list_of_pairs), expected_result)


def test_task_func_single_pair():
    list_of_pairs = [(1, 2)]
    expected_result = np.array([2])
    assert np.array_equal(task_func(list_of_pairs), expected_result)


def test_task_func_invalid_input():
    list_of_pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
    expected_result = np.array([120])
    assert np.array_equal(task_func(list_of_pairs), expected_result)