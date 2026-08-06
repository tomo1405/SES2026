import pytest
from src_0949 import task_func
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func_default_parameters():
    expected_rows = 3
    expected_columns = 2
    result = task_func()
    assert result.shape == (expected_rows, expected_columns)

def test_task_func_custom_parameters():
    rows = 5
    columns = 4
    result = task_func(rows, columns)
    assert result.shape == (rows, columns)

def test_task_func_reproducibility():
    first_run = task_func()
    second_run = task_func()
    assert np.array_equal(first_run, second_run)

def test_task_func_min_max_scaling():
    matrix = np.array([[1, 2], [3, 4], [5, 6]])
    scaler = MinMaxScaler()
    expected_scaled_matrix = scaler.fit_transform(matrix)
    result = task_func(rows=3, columns=2, seed=42)
    assert np.allclose(result, expected_scaled_matrix)

def test_task_func_zero_variance_column():
    # This test checks the behavior when there's a column with zero variance
    # which should be handled gracefully by MinMaxScaler.
    np.random.seed(42)
    matrix = np.array([[1, 1], [1, 2], [1, 3]])
    scaler = MinMaxScaler()
    expected_scaled_matrix = scaler.fit_transform(matrix)
    result = task_func(rows=3, columns=2, seed=42)
    assert np.allclose(result, expected_scaled_matrix)