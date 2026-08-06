import pytest
from src_1089 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_default_data():
    result = task_func()
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (100, 5)
    assert all(result >= 0)

def test_task_func_custom_data():
    custom_data = np.array([[0.6, 0.4, 0.7, 0.3, 0.9], [0.2, 0.8, 0.1, 0.5, 0.0]])
    result = task_func(custom_data)
    expected_result = pd.DataFrame({
        0: [0.70710678, -0.70710678],
        1: [0.0, 0.0],
        2: [1.41421356, -1.41421356],
        3: [0.0, 0.0],
        4: [1.73205081, -1.73205081]
    })
    pd.testing.assert_frame_equal(result.round(6), expected_result)

def test_task_func_all_zeros():
    custom_data = np.zeros((2, 5))
    result = task_func(custom_data)
    expected_result = pd.DataFrame(np.zeros((2, 5)), columns=[0, 1, 2, 3, 4])
    pd.testing.assert_frame_equal(result, expected_result)

def test_task_func_all_ones():
    custom_data = np.ones((2, 5))
    result = task_func(custom_data)
    expected_result = pd.DataFrame(np.zeros((2, 5)), columns=[0, 1, 2, 3, 4])
    pd.testing.assert_frame_equal(result, expected_result)

def test_task_func_large_data():
    custom_data = np.random.rand(1000, 10)
    result = task_func(custom_data)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (1000, 10)
    assert all(result >= 0)