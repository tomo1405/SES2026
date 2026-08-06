import pytest
from src_0342 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_dataframe():
    with pytest.raises(ValueError):
        task_func(None, 'column_name')

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, 'column_name')

def test_task_func_missing_column():
    df = pd.DataFrame({'col1': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, 'column_name')

def test_task_func_numeric_column():
    df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
    fig = task_func(df, 'col1')
    assert isinstance(fig, plt.Figure)

def test_task_func_categorical_column():
    df = pd.DataFrame({'col1': ['A', 'B', 'A', 'C', 'B']})
    fig = task_func(df, 'col1')
    assert isinstance(fig, plt.Figure)

def test_task_func_mixed_data_types():
    df = pd.DataFrame({
        'numeric_col': [1, 2, 3, 4, 5],
        'categorical_col': ['A', 'B', 'A', 'C', 'B']
    })
    fig_numeric = task_func(df, 'numeric_col')
    fig_categorical = task_func(df, 'categorical_col')
    assert isinstance(fig_numeric, plt.Figure)
    assert isinstance(fig_categorical, plt.Figure)