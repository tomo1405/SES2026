import pytest
from src_0415 import task_func
import pandas as pd
import numpy as np

def test_task_func_no_column_to_drop():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df_expected = pd.DataFrame(data)
    df, ax = task_func(data)
    pd.testing.assert_frame_equal(df, df_expected)
    assert ax is not None

def test_task_func_column_to_drop():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    df_expected = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    df, ax = task_func(data, column='c')
    pd.testing.assert_frame_equal(df, df_expected)
    assert ax is not None

def test_task_func_no_numeric_data():
    data = {'a': ['x', 'y', 'z'], 'b': ['p', 'q', 'r']}
    df_expected = pd.DataFrame(data)
    df, ax = task_func(data)
    pd.testing.assert_frame_equal(df, df_expected)
    assert ax is None

def test_task_func_empty_data():
    data = {}
    df_expected = pd.DataFrame()
    df, ax = task_func(data)
    pd.testing.assert_frame_equal(df, df_expected)
    assert ax is None

def test_task_func_all_numeric_data():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df_expected = pd.DataFrame(data)
    df, ax = task_func(data)
    pd.testing.assert_frame_equal(df, df_expected)
    assert ax is not None

def test_task_func_single_row():
    data = {'a': [1], 'b': [2]}
    df_expected = pd.DataFrame(data)
    df, ax = task_func(data)
    pd.testing.assert_frame_equal(df, df_expected)
    assert ax is not None

def test_task_func_single_column():
    data = {'a': [1, 2, 3]}
    df_expected = pd.DataFrame(data)
    df, ax = task_func(data)
    pd.testing.assert_frame_equal(df, df_expected)
    assert ax is not None