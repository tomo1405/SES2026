import pytest
from src_0372 import task_func
import numpy as np

def test_task_func_with_positive_values():
    input_data = np.array([1, 2, 3, 4, 5])
    expected_output = pd.DataFrame({'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]})
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_negative_values():
    input_data = np.array([-5, -4, -3, -2, -1])
    expected_output = pd.DataFrame({'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]})
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_mixed_values():
    input_data = np.array([-10, 0, 10, 20, 30])
    expected_output = pd.DataFrame({'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]})
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_single_value():
    input_data = np.array([42])
    expected_output = pd.DataFrame({'Scaled Values': [0.0]})
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_zero_variance():
    input_data = np.array([5, 5, 5, 5, 5])
    expected_output = pd.DataFrame({'Scaled Values': [0.0, 0.0, 0.0, 0.0, 0.0]})
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)