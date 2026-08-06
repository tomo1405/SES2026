import pytest
from src_1030 import task_func
import pandas as pd
import numpy as np

def test_task_func_default():
    df = task_func()
    assert df.shape == (100, 3)
    assert all(df.columns == ['a', 'b', 'c'])
    assert df.values.dtype == object

def test_task_func_custom_shape():
    df = task_func(rows=50, columns=2)
    assert df.shape == (50, 2)
    assert all(df.columns == ['a', 'b'])
    assert df.values.dtype == object

def test_task_func_column_names():
    df = task_func(columns=4)
    assert all(df.columns == ['a', 'b', 'c', 'd'])

def test_task_func_data_values():
    df = task_func(rows=1, columns=1)
    assert df.iloc[0, 0] in list("abcdefghijklmnopqrstuvwxyz")

def test_task_func_data_type():
    df = task_func()
    assert isinstance(df, pd.DataFrame)

def test_task_func_randomness():
    df1 = task_func()
    df2 = task_func()
    assert not df1.equals(df2)