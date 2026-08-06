import pytest
from src_0248 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert 'Normalized Value' in df.columns
    assert len(df) == 5000

def test_task_func_custom_parameters():
    n_data_points = 1000
    min_value = 1.0
    max_value = 9.0
    df = task_func(n_data_points, min_value, max_value)
    assert isinstance(df, pd.DataFrame)
    assert 'Normalized Value' in df.columns
    assert len(df) == n_data_points

def test_task_func_min_max_value():
    df = task_func(min_value=0.0, max_value=10.0)
    assert (df['Normalized Value'] >= -1).all() and (df['Normalized Value'] <= 1).all()

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func(min_value=10.0, max_value=0.0)

def test_task_func_data_distribution():
    df = task_func()
    assert df['Normalized Value'].mean() == pytest.approx(0.0, abs=0.1)
    assert df['Normalized Value'].std() == pytest.approx(1.0, abs=0.1)