import pytest
from src_0109 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_invalid_df():
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns."):
        task_func(pd.DataFrame())

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'group': [1, 2],
        'date': pd.date_range(start='2023-01-01', periods=2),
    })
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns."):
        task_func(df)

def test_task_func_invalid_decomposition_model():
    df = pd.DataFrame({
        'group': [1, 2],
        'date': pd.date_range(start='2023-01-01', periods=2),
        'value': [10, 20],
    })
    with pytest.raises(ValueError, match="Invalid 'decomposition_model': must be 'additive' or 'multiplicative'."):
        task_func(df, decomposition_model='invalid')

def test_task_func_invalid_freq():
    df = pd.DataFrame({
        'group': [1, 2],
        'date': pd.date_range(start='2023-01-01', periods=2),
        'value': [10, 20],
    })
    with pytest.raises(ValueError, match="Invalid 'freq': must be a string representing frequency."):
        task_func(df, freq=123)

def test_task_func_non_numeric_value():
    df = pd.DataFrame({
        'group': [1, 2],
        'date': pd.date_range(start='2023-01-01', periods=2),
        'value': ['a', 'b'],
    })
    with pytest.raises(ValueError, match="Non-numeric or missing values found in 'value' column."):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': pd.date_range(start='2023-01-01', periods=4),
        'value': [10, 20, 30, 40],
    })
    result, ax = task_func(df)
    assert isinstance(result, pd.core.series.Series)
    assert isinstance(ax, plt.Axes)