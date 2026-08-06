import pytest
from src_0244 import task_func

def test_task_func_zero_data_points():
    result = task_func(0)
    assert result.equals(pd.DataFrame(columns=['Value']))

def test_task_func_default_data_points():
    result = task_func()
    assert len(result) == 10000
    assert 'Value' in result.columns
    assert result['Value'].between(0.0, 10.0).all()

def test_task_func_custom_data_points():
    n_data_points = 5000
    result = task_func(n_data_points)
    assert len(result) == n_data_points
    assert 'Value' in result.columns
    assert result['Value'].between(0.0, 10.0).all()

def test_task_func_value_precision():
    result = task_func()
    assert result['Value'].apply(lambda x: isinstance(x, float)).all()
    assert result['Value'].apply(lambda x: round(x, 3) == x).all()