python
import pandas as pd
import numpy as np
import pytest

def task_func(data, column="c"):
    df = pd.DataFrame(data)
    if column in df.columns:
        df = df.drop(columns=column)

    # If there's no numeric data, return None for the plot.
    if df.empty or not np.any(df.dtypes.apply(pd.api.types.is_numeric_dtype)):
        return df, None

    ax = df.plot()
    return df, ax

def test_task_func():
    # Test case 1: Valid input data
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 2: Valid input data with column to drop
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    df, ax = task_func(data, column='c')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 3: Invalid input data with no numeric data
    data = {'a': ['a', 'b', 'c'], 'b': ['d', 'e', 'f']}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 4: Invalid input data with no numeric data and column to drop
    data = {'a': ['a', 'b', 'c'], 'b': ['d', 'e', 'f'], 'c': [7, 8, 9]}
    df, ax = task_func(data, column='c')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 5: Invalid input data with all non-numeric data
    data = {'a': ['a', 'b', 'c'], 'b': ['d', 'e', 'f']}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 6: Invalid input data with all non-numeric data and column to drop
    data = {'a': ['a', 'b', 'c'], 'b': ['d', 'e', 'f'], 'c': [7, 8, 9]}
    df, ax = task_func(data, column='c')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))