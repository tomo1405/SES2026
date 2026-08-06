import pytest
from src_0750 import task_func
import numpy as np

def test_task_func_with_positive_values():
    input_data = [1, 2, 3, 4, 5]
    expected_output = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_negative_values():
    input_data = [-5, -4, -3, -2, -1]
    expected_output = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_mixed_values():
    input_data = [-10, 0, 10, 20, 30]
    expected_output = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_single_value():
    input_data = [42]
    expected_output = np.array([0.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_empty_list():
    input_data = []
    expected_output = np.array([])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_float_values():
    input_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_output = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(task_func(input_data), expected_output)

def test_task_func_with_large_numbers():
    input_data = [1000000, 2000000, 3000000, 4000000, 5000000]
    expected_output = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(task_func(input_data), expected_output)