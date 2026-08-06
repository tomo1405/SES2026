import matplotlib
import pandas as pd
import pytest
from src_0982 import task_func


def test_task_func_valid_input():
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    num_series = 5
    seed = 42
    df, ax = task_func(start_date, end_date, num_series, seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_invalid_start_date():
    with pytest.raises(ValueError):
        task_func("2022-12-31", "2022-01-01", 5, 42)

def test_task_func_invalid_num_series():
    with pytest.raises(ValueError):
        task_func("2022-01-01", "2022-12-31", 0, 42)

def test_task_func_seed():
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    num_series = 5
    seed = 42
    df1, _ = task_func(start_date, end_date, num_series, seed)
    df2, _ = task_func(start_date, end_date, num_series, seed)
    assert df1.equals(df2)