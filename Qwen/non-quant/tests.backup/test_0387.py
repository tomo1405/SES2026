import pytest
from src_0387 import task_func

def test_task_func_length():
    length = 10
    df = task_func(length)
    assert len(df) == length

def test_task_func_columns():
    df = task_func(10)
    assert list(df.columns) == ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def test_task_func_min_max_values():
    min_value = 5
    max_value = 15
    df = task_func(10, min_value, max_value)
    assert df.values.min() >= min_value
    assert df.values.max() <= max_value

def test_task_func_cdf():
    df = task_func(10)
    for col in df.columns:
        assert df[col].is_monotonic_increasing

def test_task_func_empty_df():
    with pytest.raises(ValueError):
        task_func(0)