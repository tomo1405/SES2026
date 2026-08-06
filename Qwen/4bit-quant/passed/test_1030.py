import pytest
from src_1030 import task_func
import pandas as pd
import numpy as np

def test_task_func_default():
    df = task_func()
    assert df.shape == (100, 3), "Default parameters should produce a DataFrame with 100 rows and 3 columns"
    assert all(df.columns == ['a', 'b', 'c']), "Default column names should be 'a', 'b', 'c'"

def test_task_func_custom_rows_and_columns():
    df = task_func(rows=50, columns=5)
    assert df.shape == (50, 5), "Custom parameters should produce a DataFrame with 50 rows and 5 columns"
    assert all(df.columns == ['a', 'b', 'c', 'd', 'e']), "Custom column names should be 'a', 'b', 'c', 'd', 'e'"

def test_task_func_column_names():
    df = task_func(columns=4)
    assert all(df.columns == ['a', 'b', 'c', 'd']), "Column names should be generated correctly based on the number of columns"

def test_task_func_data_type():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "The returned object should be a pandas DataFrame"
    assert df.values.dtype == object, "DataFrame values should be of type object due to the random choice of characters"

def test_task_func_random_data():
    df1 = task_func()
    df2 = task_func()
    assert not df1.equals(df2), "Two consecutive calls should produce different DataFrames due to randomness"