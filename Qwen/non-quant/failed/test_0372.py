import pytest
from src_0372 import task_func
import numpy as np
import pandas as pd

def test_task_func_with_positive_values():
    input_data = np.array([1, 2, 3, 4, 5])
    expected_output = pd.DataFrame({
        'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_negative_values():
    input_data = np.array([-5, -4, -3, -2, -1])
    expected_output = pd.DataFrame({
        'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_mixed_values():
    input_data = np.array([-10, 0, 10, 20, 30])
    expected_output = pd.DataFrame({
        'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_single_value():
    input_data = np.array([42])
    expected_output = pd.DataFrame({
        'Scaled Values': [0.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_empty_array():
    input_data = np.array([])
    expected_output = pd.DataFrame(columns=['Scaled Values'])
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_one_dimensional_array():
    input_data = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    expected_output = pd.DataFrame({
        'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_float_values():
    input_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    expected_output = pd.DataFrame({
        'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)