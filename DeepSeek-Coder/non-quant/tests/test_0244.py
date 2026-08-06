import pytest
from src_0244 import task_func

def test_task_func_basic():
    result = task_func(n_data_points=10)
    assert len(result) == 10
    assert all(isinstance(val, float) for val in result['Value'])

def test_task_func_zero_data_points():
    result = task_func(n_data_points=0)
    assert result.empty

def test_task_func_large_data():
    result = task_func(n_data_points=10000)
    assert len(result) == 10000
    assert all(MIN_VALUE <= val <= MAX_VALUE for val in result['Value'])