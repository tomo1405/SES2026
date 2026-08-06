import pytest
from src_1003 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

def test_task_func_with_numeric_column():
    data = {'target_column': [1, 2, 3, 4, 5]}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert 'target_column' in df.columns
    assert df['target_column'].dtype == 'int64'
    assert isinstance(ax, plt.Axes)

def test_task_func_with_non_numeric_column():
    data = {'target_column': ['a', 'b', 'a', 'c', 'b']}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert 'target_column' in df.columns
    assert df['target_column'].dtype == 'int8'  # Assuming category codes are int8
    assert isinstance(ax, plt.Axes)

def test_task_func_with_missing_column():
    data = {'other_column': [1, 2, 3, 4, 5]}
    with pytest.raises(ValueError) as excinfo:
        task_func(data, column_name="target_column")
    assert "Column 'target_column' not found in the DataFrame." in str(excinfo.value)

def test_task_func_with_empty_data():
    data = {}
    with pytest.raises(ValueError) as excinfo:
        task_func(data, column_name="target_column")
    assert "Column 'target_column' not found in the DataFrame." in str(excinfo.value)

def test_task_func_with_single_row():
    data = {'target_column': [1]}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert 'target_column' in df.columns
    assert df['target_column'].dtype == 'int64'
    assert isinstance(ax, plt.Axes)

def test_task_func_with_multiple_columns():
    data = {'target_column': [1, 2, 3], 'other_column': ['a', 'b', 'c']}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert 'target_column' in df.columns
    assert df['target_column'].dtype == 'int64'
    assert isinstance(ax, plt.Axes)