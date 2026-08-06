import pytest
from src_0241 import task_func
import pandas as pd

def test_task_func_default():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1000
    assert df.columns[0] == 'Value'
    assert df['Value'].between(0.0, 10.0).all()
    assert df['Value'].apply(lambda x: round(x, 3) == x).all()

def test_task_func_custom_parameters():
    df = task_func(n_data_points=500, min_value=1.0, max_value=5.0, column_name='Test')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 500
    assert df.columns[0] == 'Test'
    assert df['Test'].between(1.0, 5.0).all()
    assert df['Test'].apply(lambda x: round(x, 3) == x).all()

def test_task_func_min_max_values():
    df = task_func(min_value=-10.0, max_value=10.0)
    assert df['Value'].between(-10.0, 10.0).all()

def test_task_func_zero_data_points():
    df = task_func(n_data_points=0)
    assert df.empty