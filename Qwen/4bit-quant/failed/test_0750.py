import pytest
from src_0750 import task_func
import numpy as np

def test_task_func_with_positive_numbers():
    input_data = [1, 2, 3, 4, 5]
    expected_output = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_negative_numbers():
    input_data = [-5, -4, -3, -2, -1]
    expected_output = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_mixed_numbers():
    input_data = [-10, 0, 10, 20, 30]
    expected_output = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_single_element():
    input_data = [42]
    expected_output = np.array([0.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_zero_variance():
    input_data = [5, 5, 5, 5, 5]
    expected_output = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_empty_list():
    input_data = []
    expected_output = np.array([])
    assert np.allclose(task_func(input_data), expected_output)