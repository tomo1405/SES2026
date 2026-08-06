import pytest
from src_0950 import task_func

def test_task_func_default_seed():
    df1 = task_func(3, 3)
    df2 = task_func(3, 3)
    assert not df1.equals(df2), "Without a fixed seed, outputs should differ."

def test_task_func_fixed_seed():
    df1 = task_func(3, 3, seed=42)
    df2 = task_func(3, 3, seed=42)
    assert df1.equals(df2), "With a fixed seed, outputs should be identical."

def test_task_func_zero_rows():
    df = task_func(0, 3)
    assert df.empty, "A DataFrame with zero rows should be empty."

def test_task_func_zero_columns():
    df = task_func(3, 0)
    assert df.empty, "A DataFrame with zero columns should be empty."

def test_task_func_single_row():
    df = task_func(1, 3)
    assert df.shape == (1, 3), "DataFrame shape should match the specified rows and columns."

def test_task_func_single_column():
    df = task_func(3, 1)
    assert df.shape == (3, 1), "DataFrame shape should match the specified rows and columns."

def test_task_func_large_matrix():
    df = task_func(100, 100)
    assert df.shape == (100, 100), "DataFrame shape should match the specified rows and columns."