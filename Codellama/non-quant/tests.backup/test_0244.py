import pytest
from src_0244 import task_func

def test_task_func_returns_dataframe():
    data_df = task_func()
    assert isinstance(data_df, pd.DataFrame)

def test_task_func_returns_correct_columns():
    data_df = task_func()
    assert list(data_df.columns) == ['Value']

def test_task_func_returns_correct_data_types():
    data_df = task_func()
    assert data_df['Value'].dtype == float

def test_task_func_returns_correct_number_of_rows():
    data_df = task_func(n_data_points=10)
    assert len(data_df) == 10

def test_task_func_returns_correct_data_values():
    data_df = task_func()
    assert all(data_df['Value'] >= MIN_VALUE) and all(data_df['Value'] <= MAX_VALUE)