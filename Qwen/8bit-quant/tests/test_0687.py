import pytest
from src_0687 import task_func
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def test_task_func_with_binary_values():
    input_data = [[0, 1], [1, 0]]
    expected_output = np.array([[1., 0.], [0., 1.], [0., 1.], [1., 0.]])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_multiple_classes():
    input_data = [[2, 3], [0, 1]]
    expected_output = np.array([
        [0., 0., 1., 0.],
        [0., 0., 0., 1.],
        [1., 0., 0., 0.],
        [0., 1., 0., 0.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_single_element_sublists():
    input_data = [[0], [1], [2]]
    expected_output = np.array([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_empty_input():
    input_data = []
    expected_output = np.array([])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_empty_sublists():
    input_data = [[], [], []]
    expected_output = np.array([])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_single_class():
    input_data = [[0, 0], [0, 0]]
    expected_output = np.array([
        [1., 0.],
        [1., 0.],
        [1., 0.],
        [1., 0.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)