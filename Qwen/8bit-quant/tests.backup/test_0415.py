import pytest
from src_0415 import task_func
import pandas as pd
import numpy as np

def test_task_func_no_column_to_drop():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df, ax = task_func(data)
    assert ax is not None
    assert df.equals(pd.DataFrame(data))

def test_task_func_column_to_drop():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    df, ax = task_func(data)
    assert ax is not None
    assert 'c' not in df.columns
    assert df.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}))

def test_task_func_no_numeric_data():
    data = {'a': ['x', 'y', 'z'], 'b': ['p', 'q', 'r']}
    df, ax = task_func(data)
    assert ax is None
    assert df.equals(pd.DataFrame(data))

def test_task_func_empty_data():
    data = {}
    df, ax = task_func(data)
    assert ax is None
    assert df.empty

def test_task_func_single_numeric_column():
    data = {'a': [1, 2, 3]}
    df, ax = task_func(data)
    assert ax is not None
    assert df.equals(pd.DataFrame(data))

def test_task_func_single_non_numeric_column():
    data = {'a': ['x', 'y', 'z']}
    df, ax = task_func(data)
    assert ax is None
    assert df.equals(pd.DataFrame(data))