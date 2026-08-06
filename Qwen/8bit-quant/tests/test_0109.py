import pytest
from src_0109 import task_func
import pandas as pd

def test_task_func_invalid_df():
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns."):
        task_func(pd.DataFrame({'group': [1], 'value': [1]}))

def test_task_func_missing_value_column():
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns."):
        task_func(pd.DataFrame({'group': [1], 'date': ['2023-01-01']}))

def test_task_func_invalid_decomposition_model():
    with pytest.raises(ValueError, match="Invalid 'decomposition_model': must be 'additive' or 'multiplicative'."):
        task_func(pd.DataFrame({'group': [1], 'date': ['2023-01-01'], 'value': [1]}), decomposition_model='invalid')

def test_task_func_invalid_freq():
    with pytest.raises(ValueError, match="Invalid 'freq': must be a string representing frequency."):
        task_func(pd.DataFrame({'group': [1], 'date': ['2023-01-01'], 'value': [1]}), freq=123)

def test_task_func_non_numeric_value():
    with pytest.raises(ValueError, match="Non-numeric or missing values found in 'value' column."):
        task_func(pd.DataFrame({'group': [1], 'date': ['2023-01-01'], 'value': ['a']}))

def test_task_func_valid_input():
    df = pd.DataFrame({
        'group': [1, 1],
        'date': ['2023-01-01', '2023-01-02'],
        'value': [10, 20]
    })
    result, ax = task_func(df)
    assert isinstance(result, pd.core.series.Series)
    assert isinstance(ax, plt.Axes)