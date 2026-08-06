import pytest
from src_0244 import task_func
import pandas as pd

def test_task_func_default():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10000
    assert 'Value' in df.columns
    assert df['Value'].between(0.0, 10.0).all()
    assert df['Value'].apply(lambda x: isinstance(x, float)).all()

def test_task_func_zero_data_points():
    df = task_func(0)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert 'Value' in df.columns

def test_task_func_custom_data_points():
    n_data_points = 5000
    df = task_func(n_data_points)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n_data_points
    assert 'Value' in df.columns
    assert df['Value'].between(0.0, 10.0).all()
    assert df['Value'].apply(lambda x: isinstance(x, float)).all()

def test_task_func_min_max_values():
    df = task_func()
    assert df['Value'].min() >= 0.0
    assert df['Value'].max() <= 10.0

def test_task_func_rounding():
    df = task_func()
    assert df['Value'].apply(lambda x: round(x, 3) == x).all()