import pytest
from src_0836 import task_func

def test_task_func_basic():
    df = task_func(5, [0, 2])
    assert df.shape == (5, 3)
    assert list(df.columns) == ['B', 'C', 'E']

def test_task_func_no_remove():
    df = task_func(3, [])
    assert df.shape == (3, 5)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E']

def test_task_func_remove_all():
    df = task_func(4, [0, 1, 2, 3, 4])
    assert df.shape == (4, 0)
    assert list(df.columns) == []

def test_task_func_random_seed():
    df1 = task_func(6, [1, 3], random_seed=42)
    df2 = task_func(6, [1, 3], random_seed=42)
    assert df1.equals(df2)

def test_task_func_custom_columns():
    df = task_func(7, [0, 2], columns=['X', 'Y', 'Z', 'W', 'V'])
    assert df.shape == (7, 3)
    assert list(df.columns) == ['Y', 'Z', 'V']