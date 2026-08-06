import pytest
from src_0559 import task_func
import numpy as np
import pandas as pd

def test_task_func_empty_input():
    a = []
    b = []
    df, ax = task_func(a, b)
    assert df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_non_empty_input():
    a = [1, 2, 3]
    b = [4, 5, 6]
    df, ax = task_func(a, b)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert all(df.columns == ['A', 'B'])
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_columns():
    a = [1, 2, 3]
    b = [4, 5, 6]
    columns = ['X', 'Y']
    df, ax = task_func(a, b, columns=columns)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert all(df.columns == columns)
    assert isinstance(ax, plt.Axes)

def test_task_func_single_value():
    a = [1]
    b = [4]
    df, ax = task_func(a, b)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 2)
    assert all(df.columns == ['A', 'B'])
    assert isinstance(ax, plt.Axes)

def test_task_func_different_lengths():
    a = [1, 2, 3]
    b = [4, 5]
    with pytest.raises(ValueError):
        task_func(a, b)

def test_task_func_same_values():
    a = [1, 1, 1]
    b = [2, 2, 2]
    df, ax = task_func(a, b)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert all(df.columns == ['A', 'B'])
    assert isinstance(ax, plt.Axes)