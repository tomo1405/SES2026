import pytest
from src_0976 import task_func

def test_task_func_default_parameters():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 5)
    assert list(df.columns) == ["A", "B", "C", "D", "E"]

def test_task_func_custom_columns():
    df = task_func(3, columns=["X", "Y", "Z"])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert list(df.columns) == ["X", "Y", "Z"]

def test_task_func_custom_seed():
    df1 = task_func(4, seed=42)
    df2 = task_func(4, seed=42)
    assert df1.equals(df2)

def test_task_func_duplicate_columns():
    df = task_func(2, columns=["A", "A", "B", "B"])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["A", "B"]

def test_task_func_no_columns():
    df = task_func(1, columns=[])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 0)
    assert list(df.columns) == []

def test_task_func_single_row():
    df = task_func(1)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 5)
    assert list(df.columns) == ["A", "B", "C", "D", "E"]