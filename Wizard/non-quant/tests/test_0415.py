python
import pandas as pd
import numpy as np
import pytest

from src_0415 import task_func

def test_task_func():
    # Test case 1: data with numeric values only
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 2: data with non-numeric values
    data = {'a': [1, 2, 3], 'b': ['4', '5', '6']}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 3: data with no numeric values
    data = {'a': [1, 2, 3], 'b': ['4', '5', '6']}
    df, ax = task_func(data, column='a')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 4: data with numeric values and a column to drop
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    df, ax = task_func(data, column='c')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))

    # Test case 5: data with numeric values and no column to drop
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))