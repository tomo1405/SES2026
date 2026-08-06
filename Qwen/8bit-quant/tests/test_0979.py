import pytest
from src_0979 import task_func
import numpy as np
import pandas as pd

def test_task_func_invalid_input_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_empty_array():
    result = task_func(np.array([]))
    assert result.equals(pd.DataFrame(columns=["PC1", "PC2"]))

def test_task_func_zero_column_array():
    result = task_func(np.array([[1], [2], [3]]))
    assert result.equals(pd.DataFrame(columns=["PC1", "PC2"]))

def test_task_func_2d_array_with_seed():
    np.random.seed(42)
    array = np.array([[1, 2], [3, 4], [5, 6]])
    result = task_func(array, seed=42)
    expected = pd.DataFrame({
        "PC1": [-1.22474487, 0., 1.22474487],
        "PC2": [-0.70710678, 0.70710678, -0.70710678]
    })
    pd.testing.assert_frame_equal(result, expected, check_less_precise=1)

def test_task_func_2d_array_without_seed():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    result = task_func(array)
    assert result.shape == (3, 2)

def test_task_func_single_column_array():
    array = np.array([[1], [2], [3]])
    result = task_func(array)
    assert result.shape == (3, 1)
    assert list(result.columns) == ["PC1"]

def test_task_func_more_than_two_columns():
    np.random.seed(42)
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    result = task_func(array, seed=42)
    expected = pd.DataFrame({
        "PC1": [-1.22474487, 0., 1.22474487],
        "PC2": [-0.70710678, 0.70710678, -0.70710678]
    })
    pd.testing.assert_frame_equal(result, expected, check_less_precise=1)