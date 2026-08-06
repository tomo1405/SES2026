import pytest
from src_1139 import task_func
import numpy as np

def test_task_func_with_empty_matrix():
    matrix = np.array([])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([]))
    assert combinations == []

def test_task_func_with_single_element_matrix():
    matrix = np.array([5])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([5]))
    assert combinations == []

def test_task_func_with_two_elements_matrix():
    matrix = np.array([3, 1])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([1, 3]))
    assert combinations == [(1, 3)]

def test_task_func_with_multiple_elements_matrix():
    matrix = np.array([4, 1, 3, 2])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([1, 2, 3, 4]))
    expected_combinations = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    assert combinations == expected_combinations

def test_task_func_with_negative_and_positive_elements():
    matrix = np.array([-1, 2, -3, 4])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([-3, -1, 2, 4]))
    expected_combinations = [(-3, -1), (-3, 2), (-3, 4), (-1, 2), (-1, 4), (2, 4)]
    assert combinations == expected_combinations

def test_task_func_with_duplicate_elements():
    matrix = np.array([2, 2, 1, 1])
    sorted_array, combinations = task_func(matrix)
    assert np.array_equal(sorted_array, np.array([1, 1, 2, 2]))
    expected_combinations = [(1, 1), (1, 2), (1, 2), (2, 2)]
    assert combinations == expected_combinations