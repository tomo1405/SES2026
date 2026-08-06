import pytest
from src_0244 import task_func

def test_task_func_returns_dataframe():
    result = task_func()
    assert isinstance(result, pd.DataFrame)

def test_task_func_returns_correct_columns():
    result = task_func()
    assert list(result.columns) == ['Value']

def test_task_func_returns_correct_data_types():
    result = task_func()
    assert result['Value'].dtype == float

def test_task_func_returns_correct_number_of_rows():
    result = task_func(n_data_points=10)
    assert len(result) == 10

def test_task_func_returns_correct_data_values():
    result = task_func()
    assert all(result['Value'] >= MIN_VALUE) and all(result['Value'] <= MAX_VALUE)