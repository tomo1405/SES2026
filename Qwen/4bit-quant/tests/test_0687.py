import pytest
from src_0687 import task_func
import numpy as np

def test_task_func_with_binary_values():
    input_data = [[0, 1], [1, 0], [0, 0]]
    expected_output = np.array([
        [1., 0.],
        [0., 1.],
        [1., 0.],
        [0., 1.],
        [1., 0.],
        [1., 0.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_single_value():
    input_data = [[2]]
    expected_output = np.array([[0., 0., 1.]])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_empty_list():
    input_data = []
    expected_output = np.array([])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_multiple_sublists():
    input_data = [[0, 1, 2], [3, 4], [5]]
    expected_output = np.array([
        [1., 0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 1.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_negative_values():
    input_data = [[-1, -2], [-2, -1]]
    expected_output = np.array([
        [0., 0., 1., 0.],
        [0., 0., 0., 1.],
        [0., 0., 0., 1.],
        [0., 0., 1., 0.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)