import pytest
from src_0441 import task_func
import numpy as np
import pandas as pd

def test_task_func_empty_input():
    P = np.array([])
    T = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError, match="Inputs cannot be empty."):
        task_func(P, T)

def test_task_func_incompatible_shapes():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([1, 2])
    with pytest.raises(ValueError, match="Matrix P shape 2 and Tensor T shape 2 are incompatible for tensor multiplication."):
        task_func(P, T)

def test_task_func_valid_input():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[1, 2], [3, 4]])
    result = task_func(P, T)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 4)
    assert all(result.columns == [f"feature_{i}" for i in range(4)])

def test_task_func_result_values():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[1, 2], [3, 4]])
    result = task_func(P, T)
    expected_mean = 0
    expected_std = 1
    assert np.isclose(result.mean().values, expected_mean, atol=1e-5).all()
    assert np.isclose(result.std().values, expected_std, atol=1e-5).all()

def test_task_func_single_row_P():
    P = np.array([[1, 2]])
    T = np.array([[1, 2], [3, 4]])
    result = task_func(P, T)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (1, 4)
    assert all(result.columns == [f"feature_{i}" for i in range(4)])

def test_task_func_single_column_T():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[1], [2]])
    result = task_func(P, T)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 2)
    assert all(result.columns == [f"feature_{i}" for i in range(2)])