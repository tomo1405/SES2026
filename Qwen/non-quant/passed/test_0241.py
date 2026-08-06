import pytest
from src_0241 import task_func
import pandas as pd

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1000
    assert 'Value' in df.columns
    assert all(0.0 <= value <= 10.0 for value in df['Value'])

def test_task_func_custom_parameters():
    n_data_points = 500
    min_value = 5.0
    max_value = 15.0
    column_name = 'CustomValue'
    df = task_func(n_data_points, min_value, max_value, column_name)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n_data_points
    assert column_name in df.columns
    assert all(min_value <= value <= max_value for value in df[column_name])

def test_task_func_min_max_values():
    df = task_func(min_value=0.0, max_value=0.0)
    assert all(value == 0.0 for value in df['Value'])

    df = task_func(min_value=10.0, max_value=10.0)
    assert all(value == 10.0 for value in df['Value'])

def test_task_func_rounding():
    df = task_func(n_data_points=1, min_value=0.0, max_value=1.0)
    value = df['Value'].iloc[0]
    assert isinstance(value, float)
    assert len(str(value).split('.')[1]) <= 3