import pytest
from src_0087 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_students():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 2)
    assert list(df.columns) == ["Student", "Score"]
    assert all(df["Student"].isin(["Alice", "Bob", "Charlie", "David", "Eve"]))
    assert df.is_sorted_values_equal(by="Score")

def test_task_func_custom_students():
    custom_students = ["Zara", "Liam", "Olivia"]
    df, ax = task_func(custom_students, seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert list(df.columns) == ["Student", "Score"]
    assert all(df["Student"].isin(custom_students))
    assert df.is_sorted_values_equal(by="Score")

def test_task_func_seed_consistency():
    df1, _ = task_func(seed=42)
    df2, _ = task_func(seed=42)
    assert df1.equals(df2)

def test_task_func_score_range():
    df, _ = task_func()
    assert all(0 <= score <= 100 for score in df["Score"])

def test_task_func_plot_ylabel():
    _, ax = task_func()
    assert ax.get_ylabel() == "Score"