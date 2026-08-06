import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0094 import task_func


def test_task_func_invalid_n_components():
    data = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError, match="n_components must be a positive integer"):
        task_func(data, n_components=-1)

def test_task_func_non_integer_n_components():
    data = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError, match="n_components must be a positive integer"):
        task_func(data, n_components=2.5)

def test_task_func_zero_n_components():
    data = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError, match="n_components must be a positive integer"):
        task_func(data, n_components=0)

def test_task_func_valid_n_components():
    data = np.array([[1, 2], [3, 4]])
    df, ax = task_func(data, n_components=2)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ['PC1', 'PC2']
    assert isinstance(ax, plt.Axes)

def test_task_func_single_component():
    data = np.array([[1, 2], [3, 4]])
    df, ax = task_func(data, n_components=1)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 1)
    assert list(df.columns) == ['PC1']
    assert isinstance(ax, plt.Axes)

def test_task_func_random_seed():
    data = np.array([[1, 2], [3, 4]])
    df1, _ = task_func(data, n_components=2)
    df2, _ = task_func(data, n_components=2)
    assert df1.equals(df2)