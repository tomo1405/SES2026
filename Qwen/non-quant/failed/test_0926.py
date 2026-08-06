import pytest
from src_0926 import task_func

def test_task_func_default_parameters():
    df = task_func()
    assert df.shape == (1000, 5)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E']
    assert df.values.min() >= -1
    assert df.values.max() <= 100

def test_task_func_custom_parameters():
    df = task_func(data_size=500, column_names=['X', 'Y'], seed=42)
    assert df.shape == (500, 2)
    assert list(df.columns) == ['X', 'Y']
    assert df.values.min() >= -1
    assert df.values.max() <= 100

def test_task_func_negative_values_replacement():
    df = task_func(seed=0)
    assert (df[df < 10] == -1).all().all()

def test_task_func_random_state_consistency():
    df1 = task_func(seed=0)
    df2 = task_func(seed=0)
    assert df1.equals(df2)

def test_task_func_large_data_size():
    df = task_func(data_size=10000, seed=0)
    assert df.shape == (10000, 5)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E']
    assert df.values.min() >= -1
    assert df.values.max() <= 100