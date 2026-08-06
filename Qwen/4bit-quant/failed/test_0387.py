import pytest
from src_0387 import task_func

def test_task_func_length():
    length = 10
    df = task_func(length)
    assert len(df) == length, "The DataFrame length should match the input length."

def test_task_func_columns():
    df = task_func(10)
    assert list(df.columns) == COLUMNS, "The DataFrame columns should match the predefined COLUMNS."

def test_task_func_min_max_values():
    min_value = 10
    max_value = 20
    df = task_func(10, min_value=min_value, max_value=max_value)
    assert df.min().min() >= min_value, "The minimum value in the DataFrame should be greater than or equal to the min_value."
    assert df.max().max() <= max_value, "The maximum value in the DataFrame should be less than or equal to the max_value."

def test_task_func_cdf_values():
    df = task_func(10)
    assert all(df.iloc[-1] == 1), "The last row of the DataFrame should be all ones since it represents the CDF."

def test_task_func_empty_df():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)