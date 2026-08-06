import pytest
from src_0926 import task_func

def test_task_func_default_parameters():
    df = task_func()
    assert df.shape == (1000, 5)
    assert all(df.columns == ['A', 'B', 'C', 'D', 'E'])

def test_task_func_custom_parameters():
    df = task_func(data_size=500, column_names=['X', 'Y'], seed=42)
    assert df.shape == (500, 2)
    assert all(df.columns == ['X', 'Y'])

def test_task_func_value_replacement():
    df = task_func(seed=0)
    assert (df < 10).sum().sum() == 0, "Values less than 10 should be replaced with -1"

def test_task_func_randomness():
    df1 = task_func(seed=0)
    df2 = task_func(seed=0)
    assert df1.equals(df2), "DataFrames should be identical with the same seed"

def test_task_func_negative_values():
    df = task_func(seed=0)
    assert (df == -1).sum().sum() > 0, "There should be at least one value replaced with -1"