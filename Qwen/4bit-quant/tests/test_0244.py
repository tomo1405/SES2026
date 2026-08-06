import pandas as pd
from src_0244 import task_func


def test_task_func_default():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10000
    assert 'Value' in df.columns

def test_task_func_zero_data_points():
    df = task_func(0)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert 'Value' in df.columns

def test_task_func_custom_data_points():
    n_data_points = 100
    df = task_func(n_data_points)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n_data_points
    assert 'Value' in df.columns

def test_task_func_value_range():
    df = task_func()
    values = df['Value']
    assert values.min() >= 0.0
    assert values.max() <= 10.0

def test_task_func_value_precision():
    df = task_func()
    values = df['Value']
    assert all(isinstance(value, float) and len(str(value).split('.')[1]) == 3 for value in values)