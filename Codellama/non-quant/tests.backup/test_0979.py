import pytest
from src_0979 import task_func
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def test_task_func_valid_input():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    df = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ["PC1", "PC2"]

def test_task_func_invalid_input():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        task_func(array, seed=123)

def test_task_func_empty_input():
    array = np.array([])
    df = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (0, 2)
    assert df.columns.tolist() == ["PC1", "PC2"]

def test_task_func_zero_columns():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    df = task_func(array, seed=123)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ["PC1", "PC2"]

def test_task_func_shuffled_array():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    df = task_func(array, seed=123)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ["PC1", "PC2"]