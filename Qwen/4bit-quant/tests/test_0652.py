import pytest
from src_0652 import task_func
import pandas as pd

def test_task_func_with_non_empty_dataframe():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [1, 2, 3, 4]
    })
    target_value = '2'
    counts, ax = task_func(df, target_value)
    assert isinstance(counts, pd.Series)
    assert counts['A'] == 1
    assert counts['B'] == 1
    assert ax is not None

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    target_value = '2'
    counts, ax = task_func(df, target_value)
    assert counts.empty
    assert ax is None

def test_task_func_with_non_numeric_target_value():
    df = pd.DataFrame({
        'A': ['a', 'b', 'c', 'd'],
        'B': ['a', 'b', 'c', 'd']
    })
    target_value = 'b'
    counts, ax = task_func(df, target_value)
    assert isinstance(counts, pd.Series)
    assert counts['A'] == 1
    assert counts['B'] == 1
    assert ax is not None

def test_task_func_with_numeric_target_value():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [1, 2, 3, 4]
    })
    target_value = '2'
    counts, ax = task_func(df, target_value)
    assert isinstance(counts, pd.Series)
    assert counts['A'] == 1
    assert counts['B'] == 1
    assert ax is not None

def test_task_func_with_mixed_data_types():
    df = pd.DataFrame({
        'A': [1, '2', 3, 4],
        'B': ['1', 2, 3, '4']
    })
    target_value = '2'
    counts, ax = task_func(df, target_value)
    assert isinstance(counts, pd.Series)
    assert counts['A'] == 1
    assert counts['B'] == 1
    assert ax is not None