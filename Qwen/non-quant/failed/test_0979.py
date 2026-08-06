import pytest
from src_0979 import task_func
import numpy as np
import pandas as pd

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])  # Not a 2D numpy array

    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]).reshape(-1))  # Not a 2D numpy array

    with pytest.raises(ValueError):
        task_func(np.array([]))  # Empty array

    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4], [5, 6]]), seed=42)  # Array with shape (3, 2)

def test_task_func_empty_array():
    result = task_func(np.array([[1, 2], [3, 4]]), seed=42)
    assert result.equals(pd.DataFrame(columns=["PC1", "PC2"]))

def test_task_func_single_column():
    array = np.array([[1], [2], [3]])
    result = task_func(array, seed=42)
    assert result.equals(pd.DataFrame(columns=["PC1"]))

def test_task_func_two_columns():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    result = task_func(array, seed=42)
    assert result.columns.tolist() == ["PC1", "PC2"]
    assert result.shape == (3, 2)

def test_task_func_more_than_two_columns():
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    result = task_func(array, seed=42)
    assert result.columns.tolist() == ["PC1", "PC2"]
    assert result.shape == (3, 2)

def test_task_func_with_seed():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    result1 = task_func(array, seed=42)
    result2 = task_func(array, seed=42)
    assert result1.equals(result2)

def test_task_func_without_seed():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    result1 = task_func(array)
    result2 = task_func(array)
    assert not result1.equals(result2)