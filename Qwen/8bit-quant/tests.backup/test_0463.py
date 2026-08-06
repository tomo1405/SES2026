import pytest
from src_0463 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert set(df.columns) == {"Category", "Value"}
    assert set(df["Category"].unique()) <= set(["a", "b", "c", "d", "e"])
    assert all(1 <= value <= 100 for value in df["Value"])
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_parameters():
    df, ax = task_func(num_rows=50, categories=["x", "y"], random_seed=123)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 50
    assert set(df.columns) == {"Category", "Value"}
    assert set(df["Category"].unique()) <= set(["x", "y"])
    assert all(1 <= value <= 100 for value in df["Value"])
    assert isinstance(ax, plt.Axes)

def test_task_func_negative_num_rows():
    with pytest.raises(ValueError, match="num_rows must not be negative"):
        task_func(num_rows=-10)

def test_task_func_zero_num_rows():
    with pytest.raises(ValueError, match="num_rows must not be negative"):
        task_func(num_rows=0)

def test_task_func_empty_categories():
    with pytest.raises(IndexError):
        task_func(categories=[])

def test_task_func_single_category():
    df, ax = task_func(categories=["z"])
    assert set(df["Category"].unique()) == set(["z"])