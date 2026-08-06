import pytest
from src_0976 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_columns():
    df = task_func(5)
    assert list(df.columns) == ["A", "B", "C", "D", "E"]
    assert df.shape == (5, 5)

def test_task_func_custom_columns():
    df = task_func(3, columns=["X", "Y", "Z"])
    assert list(df.columns) == ["X", "Y", "Z"]
    assert df.shape == (3, 3)

def test_task_func_duplicate_columns():
    df = task_func(4, columns=["A", "A", "B", "C"])
    assert list(df.columns) == ["A", "B", "C"]
    assert df.shape == (4, 3)

def test_task_func_empty_columns():
    with pytest.raises(ValueError):
        task_func(2, columns=[])

def test_task_func_randomness():
    df1 = task_func(2, seed=0)
    df2 = task_func(2, seed=0)
    pd.testing.assert_frame_equal(df1, df2)

def test_task_func_different_seed():
    df1 = task_func(2, seed=0)
    df2 = task_func(2, seed=1)
    assert not df1.equals(df2)

def test_task_func_non_default_seed():
    df = task_func(3, seed=42)
    assert df.shape == (3, 5)