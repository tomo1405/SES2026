import pytest
from src_0688 import task_func
import numpy as np
from scipy.stats import mode

def test_task_func_with_single_element():
    input_data = [[1]]
    expected_output = (np.array([1]), np.array([1]))
    assert task_func(input_data) == expected_output

def test_task_func_with_multiple_elements():
    input_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = (np.array([1]), np.array([1]))
    assert task_func(input_data) == expected_output

def test_task_func_with_repeated_elements():
    input_data = [[1, 2, 2], [2, 3, 3], [3, 3, 4]]
    expected_output = (np.array([3]), np.array([3]))
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_sublists():
    input_data = [[], [1, 2, 3], [], [4, 5]]
    expected_output = (np.array([1]), np.array([1]))
    assert task_func(input_data) == expected_output

def test_task_func_with_all_same_elements():
    input_data = [[1, 1, 1], [1, 1], [1]]
    expected_output = (np.array([1]), np.array([6]))
    assert task_func(input_data) == expected_output

def test_task_func_with_floats():
    input_data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    expected_output = (np.array([1.0]), np.array([1]))
    assert task_func(input_data) == expected_output

def test_task_func_with_mixed_integers_and_floats():
    input_data = [[1, 2.0, 3], [4, 5.0, 6], [7, 8.0, 9]]
    expected_output = (np.array([1]), np.array([1]))
    assert task_func(input_data) == expected_output