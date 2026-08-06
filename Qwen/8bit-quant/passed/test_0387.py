import pytest
from src_0387 import task_func

def test_task_func_length():
    length = 5
    df = task_func(length)
    assert len(df) == length

def test_task_func_columns():
    df = task_func(5)
    assert list(df.columns) == ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def test_task_func_min_max_values():
    min_value = 10
    max_value = 20
    df = task_func(5, min_value=min_value, max_value=max_value)
    assert df.values.min() >= min_value
    assert df.values.max() <= max_value

def test_task_func_cdf():
    df = task_func(5)
    for column in df.columns:
        assert df[column].is_monotonic_increasing

def test_task_func_default_values():
    df = task_func(5)
    assert df.values.min() >= 0
    assert df.values.max() <= 100