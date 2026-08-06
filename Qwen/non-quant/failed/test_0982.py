import pytest
from src_0982 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_valid_dates():
    df, ax = task_func("2023-01-01", "2023-01-10", 3)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert len(df.columns) == 3
    assert all(col.startswith("series_") for col in df.columns)

def test_task_func_invalid_dates():
    with pytest.raises(ValueError):
        task_func("2023-01-10", "2023-01-01", 3)

def test_task_func_zero_series():
    with pytest.raises(ValueError):
        task_func("2023-01-01", "2023-01-10", 0)

def test_task_func_one_series():
    df, ax = task_func("2023-01-01", "2023-01-10", 1)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert len(df.columns) == 1
    assert df.columns[0] == "series_1"

def test_task_func_with_seed():
    df1, ax1 = task_func("2023-01-01", "2023-01-10", 3, seed=42)
    df2, ax2 = task_func("2023-01-01", "2023-01-10", 3, seed=42)
    assert df1.equals(df2)

def test_task_func_plot(ax):
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Random Time Series"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Value"