import pytest
from src_1089 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_default_input():
    result = task_func()
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (100, 5)

def test_task_func_custom_input():
    custom_data = np.array([[0.1, 0.6, 0.2, 0.8, 0.4],
                            [0.9, 0.3, 0.7, 0.5, 0.0]])
    expected_output = np.array([[0., 0., 0., 0.84162123, 0.],
                                [1.78885438, 0., 1.16189501, 0., -0.84162123]])
    result = task_func(custom_data).values
    np.testing.assert_array_almost_equal(result, expected_output, decimal=6)

def test_task_func_negative_values():
    custom_data = np.array([[-0.1, 0.6, -0.2, 0.8, 0.4],
                            [0.9, -0.3, 0.7, 0.5, -0.0]])
    expected_output = np.array([[0., 0., 0., 0.84162123, 0.],
                                [1.78885438, 0., 1.16189501, 0., -0.84162123]])
    result = task_func(custom_data).values
    np.testing.assert_array_almost_equal(result, expected_output, decimal=6)

def test_task_func_all_zeros():
    custom_data = np.zeros((2, 5))
    expected_output = np.zeros((2, 5))
    result = task_func(custom_data).values
    np.testing.assert_array_almost_equal(result, expected_output, decimal=6)

def test_task_func_all_ones():
    custom_data = np.ones((2, 5))
    scaler = StandardScaler()
    expected_output = scaler.fit_transform(np.ones((2, 5)))
    result = task_func(custom_data).values
    np.testing.assert_array_almost_equal(result, expected_output, decimal=6)