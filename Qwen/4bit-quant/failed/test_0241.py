import pytest
from src_0241 import task_func
import pandas as pd

def test_task_func_default():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1000
    assert df.columns[0] == 'Value'
    assert all(0.0 <= value <= 10.0 for value in df['Value'])

def test_task_func_custom_params():
    df = task_func(n_data_points=500, min_value=5.0, max_value=15.0, column_name='CustomValue')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 500
    assert df.columns[0] == 'CustomValue'
    assert all(5.0 <= value <= 15.0 for value in df['CustomValue'])

def test_task_func_single_point():
    df = task_func(n_data_points=1)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df.columns[0] == 'Value'

def test_task_func_no_data_points():
    with pytest.raises(ValueError):
        task_func(n_data_points=0)

def test_task_func_negative_min_value():
    with pytest.raises(ValueError):
        task_func(min_value=-1.0, max_value=0.0)

def test_task_func_max_value_less_than_min_value():
    with pytest.raises(ValueError):
        task_func(min_value=10.0, max_value=5.0)