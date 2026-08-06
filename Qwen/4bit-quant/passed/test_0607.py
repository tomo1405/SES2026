import pytest
from src_0607 import task_func
import numpy as np

def test_task_func_with_valid_data():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = np.array([
        [-1.22474487, -1.22474487, -1.22474487],
        [0., 0., 0.],
        [1.22474487, 1.22474487, 1.22474487]
    ])
    result = task_func(matrix).values
    assert np.allclose(result, expected_result, atol=1e-8)

def test_task_func_with_nan_values():
    matrix = [[1, 2, np.nan], [4, 5, 6], [7, 8, 9]]
    expected_result = np.array([
        [-1.22474487, -1.22474487, 0.0],
        [0., 0., 0.],
        [1.22474487, 1.22474487, 0.0]
    ])
    result = task_func(matrix).values
    assert np.allclose(result, expected_result, atol=1e-8)

def test_task_func_with_single_row():
    matrix = [[1, 2, 3]]
    expected_result = np.array([[0., 0., 0.]])
    result = task_func(matrix).values
    assert np.allclose(result, expected_result, atol=1e-8)

def test_task_func_with_single_column():
    matrix = [[1], [2], [3]]
    expected_result = np.array([[0.], [0.], [0.]])
    result = task_func(matrix).values
    assert np.allclose(result, expected_result, atol=1e-8)

def test_task_func_with_empty_matrix():
    matrix = []
    expected_result = np.array([])
    result = task_func(matrix).values
    assert np.allclose(result, expected_result, atol=1e-8)