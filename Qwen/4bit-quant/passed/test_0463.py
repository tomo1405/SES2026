import pytest
from src_0463 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert "Category" in df.columns
    assert "Value" in df.columns
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_num_rows():
    df, ax = task_func(num_rows=50)
    assert len(df) == 50

def test_task_func_custom_categories():
    df, ax = task_func(categories=["x", "y", "z"])
    assert df["Category"].isin(["x", "y", "z"]).all()

def test_task_func_custom_random_seed():
    df1, _ = task_func(random_seed=123)
    df2, _ = task_func(random_seed=123)
    assert df1.equals(df2)

def test_task_func_negative_num_rows():
    with pytest.raises(ValueError):
        task_func(num_rows=-10)

def test_task_func_zero_num_rows():
    with pytest.raises(ValueError):
        task_func(num_rows=0)