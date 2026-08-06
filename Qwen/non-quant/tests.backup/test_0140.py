import pytest
from src_0140 import task_func
import pandas as pd
import numpy as np

def test_task_func_empty_df():
    with pytest.raises(ValueError, match="The input must be a non-empty pandas DataFrame."):
        task_func(pd.DataFrame())

def test_task_func_non_df_input():
    with pytest.raises(ValueError, match="The input must be a non-empty pandas DataFrame."):
        task_func([1, 2, 3])

def test_task_func_no_numeric_columns():
    df = pd.DataFrame({'A': ['a', 'b'], 'B': ['c', 'd']})
    with pytest.raises(ValueError, match="DataFrame contains no numeric columns."):
        task_func(df)

def test_task_func_with_numeric_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    axes = task_func(df)
    assert len(axes) == 2
    assert all(isinstance(ax, plt.Axes) for ax in axes)

def test_task_func_with_mixed_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [4.0, 5.0, 6.0]})
    axes = task_func(df)
    assert len(axes) == 2
    assert all(isinstance(ax, plt.Axes) for ax in axes)