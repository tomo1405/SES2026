import pytest
from src_0478 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_default_values():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 3)
    assert list(df.columns) == ["x", "y", "category"]
    assert all(df["category"].isin(["A", "B", "C", "D", "E"]))

def test_task_func_custom_N():
    df, ax = task_func(N=50)
    assert df.shape == (50, 3)

def test_task_func_custom_CATEGORIES():
    df, ax = task_func(CATEGORIES=["X", "Y", "Z"])
    assert all(df["category"].isin(["X", "Y", "Z"]))

def test_task_func_custom_seed():
    df1, _ = task_func(seed=123)
    df2, _ = task_func(seed=123)
    assert df1.equals(df2)

def test_task_func_N_less_than_categories():
    df, ax = task_func(N=3)
    assert df["category"].nunique() == 3

def test_task_func_N_greater_than_categories():
    df, ax = task_func(N=15)
    assert df["category"].nunique() == 5

def test_task_func_plot(ax):
    df, ax = task_func()
    assert isinstance(ax, plt.Axes)
    for category in ["A", "B", "C", "D", "E"]:
        assert any(line.get_label() == category for line in ax.get_lines())