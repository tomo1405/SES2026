import pytest
from src_0687 import task_func
import numpy as np

def test_task_func_with_binary_data():
    input_data = [[0, 1], [1, 0]]
    expected_output = np.array([
        [1., 0.],
        [0., 1.],
        [0., 1.],
        [1., 0.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_categorical_data():
    input_data = [['cat'], ['dog'], ['bird']]
    expected_output = np.array([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_single_element():
    input_data = [[42]]
    expected_output = np.array([[1.]])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_empty_sublists():
    input_data = [[], [1, 2], [], [3]]
    expected_output = np.array([
        [1.],
        [2.],
        [3.]
    ])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_empty_input():
    input_data = []
    expected_output = np.array([])
    assert np.array_equal(task_func(input_data), expected_output)