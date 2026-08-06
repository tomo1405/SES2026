import pandas as pd
from src_0976 import task_func


def test_task_func_default():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 5)
    assert list(df.columns) == ["A", "B", "C", "D", "E"]

def test_task_func_custom_columns():
    df = task_func(3, columns=["X", "Y", "Z"])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert list(df.columns) == ["X", "Y", "Z"]

def test_task_func_different_seed():
    df1 = task_func(4, seed=1)
    df2 = task_func(4, seed=1)
    assert df1.equals(df2)

def test_task_func_unique_columns():
    df = task_func(4, columns=["A", "A", "B", "C", "C", "D"])
    assert len(df.columns) == 4
    assert list(df.columns) == ["A", "B", "C", "D"]

def test_task_func_no_columns():
    df = task_func(2, columns=[])
    assert df.empty
    assert df.shape == (2, 0)

def test_task_func_single_row():
    df = task_func(1)
    assert df.shape == (1, 5)
    assert list(df.columns) == ["A", "B", "C", "D", "E"]

def test_task_func_single_column():
    df = task_func(3, columns=["Single"])
    assert df.shape == (3, 1)
    assert list(df.columns) == ["Single"]