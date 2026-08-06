import pytest
from src_1030 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 3)
    assert list(df.columns) == ['a', 'b', 'c']

def test_task_func_custom_rows_and_columns():
    df = task_func(rows=50, columns=2)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50, 2)
    assert list(df.columns) == ['a', 'b']

def test_task_func_column_names():
    df = task_func(columns=4)
    assert list(df.columns) == ['a', 'b', 'c', 'd']

def test_task_func_data_values():
    df = task_func(rows=10, columns=1)
    assert all(df.iloc[:, 0].isin(list("abcdefghijklmnopqrstuvwxyz")))

def test_task_func_empty_dataframe():
    with pytest.raises(ValueError):
        task_func(rows=0, columns=3)

def test_task_func_negative_rows():
    with pytest.raises(ValueError):
        task_func(rows=-10, columns=3)

def test_task_func_negative_columns():
    with pytest.raises(ValueError):
        task_func(rows=10, columns=-3)