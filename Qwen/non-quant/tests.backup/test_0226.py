import pytest
from src_0226 import task_func
import pandas as pd

def test_task_func_basic():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 'one', 2: 'two'}
    result = task_func(df, dct)
    assert result.equals(pd.DataFrame({'A': ['one', 'two', 3], 'B': [4, 5, 6]}))

def test_task_func_no_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 'one', 2: 'two'}
    result = task_func(df, dct, plot_histograms=True)
    assert result.equals(pd.DataFrame({'A': ['one', 'two', 3], 'B': [4, 5, 6]}))

def test_task_func_with_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 'one', 2: 'two'}
    result = task_func(df, dct, columns=['A'], plot_histograms=True)
    assert result.equals(pd.DataFrame({'A': ['one', 'two', 3], 'B': [4, 5, 6]}))

def test_task_func_invalid_df():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], {})

def test_task_func_empty_df():
    df = pd.DataFrame()
    dct = {1: 'one', 2: 'two'}
    result = task_func(df, dct)
    assert result.equals(pd.DataFrame())

def test_task_func_no_replacement():
    df = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
    dct = {1: 'one', 2: 'two'}
    result = task_func(df, dct)
    assert result.equals(pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]}))