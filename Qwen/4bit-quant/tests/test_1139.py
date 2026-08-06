import numpy as np
from src_1139 import task_func


def test_task_func_with_empty_matrix():
    matrix = np.array([])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([]))
    assert combinations == []

def test_task_func_with_single_element():
    matrix = np.array([5])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([5]))
    assert combinations == []

def test_task_func_with_two_elements():
    matrix = np.array([3, 1])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([1, 3]))
    assert combinations == [(1, 3)]

def test_task_func_with_multiple_elements():
    matrix = np.array([4, 1, 7, 3])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([1, 3, 4, 7]))
    expected_combinations = [(1, 3), (1, 4), (1, 7), (3, 4), (3, 7), (4, 7)]
    assert combinations == expected_combinations

def test_task_func_with_negative_numbers():
    matrix = np.array([-2, -5, 0, 3])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([-5, -2, 0, 3]))
    expected_combinations = [(-5, -2), (-5, 0), (-5, 3), (-2, 0), (-2, 3), (0, 3)]
    assert combinations == expected_combinations

def test_task_func_with_duplicate_elements():
    matrix = np.array([2, 2, 1, 1])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([1, 1, 2, 2]))
    expected_combinations = [(1, 1), (1, 2), (1, 2), (2, 2)]
    assert combinations == expected_combinations