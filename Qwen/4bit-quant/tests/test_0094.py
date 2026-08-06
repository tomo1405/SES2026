import pytest
from src_0094 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func_with_default_n_components():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert list(df.columns) == ['PC1', 'PC2']
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_n_components():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df, ax = task_func(data, n_components=1)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 1)
    assert list(df.columns) == ['PC1']
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_n_components():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError, match="n_components must be a positive integer"):
        task_func(data, n_components=-1)

def test_task_func_with_zero_n_components():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError, match="n_components must be a positive integer"):
        task_func(data, n_components=0)

def test_task_func_with_non_integer_n_components():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError, match="n_components must be a positive integer"):
        task_func(data, n_components=2.5)

def test_task_func_with_empty_data():
    data = np.array([])
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_single_row_data():
    data = np.array([[1, 2]])
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 2)
    assert list(df.columns) == ['PC1', 'PC2']
    assert isinstance(ax, plt.Axes)

def test_task_func_with_single_column_data():
    data = np.array([[1], [2], [3]])
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 1)
    assert list(df.columns) == ['PC1']
    assert isinstance(ax, plt.Axes)