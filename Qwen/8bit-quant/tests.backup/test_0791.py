import pytest
from src_0791 import task_func
import pandas as pd
import numpy as np

def test_task_func_basic():
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2')
    assert result == [0, 4, 1, 3, 2]

def test_task_func_with_N_less_than_data_length():
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2', N=3)
    assert len(result) == 3

def test_task_func_with_N_equal_to_data_length():
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2', N=5)
    assert len(result) == 5

def test_task_func_with_identical_columns():
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2')
    assert all(diff == 0 for diff in np.abs(df['col1'].values - df['col2'].values))
    assert result == []

def test_task_func_with_negative_values():
    data = {
        'col1': [-1, -2, -3, -4, -5],
        'col2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2')
    assert result == [0, 4, 1, 3, 2]

def test_task_func_with_missing_columns():
    data = {
        'col1': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError) as excinfo:
        task_func(df, 'col1', 'col2')
    assert "Columns col2 not found in the DataFrame." in str(excinfo.value)

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(df, 'col1', 'col2')
    assert "Columns col1 or col2 not found in the DataFrame." in str(excinfo.value)