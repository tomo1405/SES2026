import pytest
from src_0982 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_valid_dates_and_num_series():
    start_date = "2023-01-01"
    end_date = "2023-01-10"
    num_series = 3
    df, ax = task_func(start_date, end_date, num_series)
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == num_series
    assert len(df.index) == (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days + 1
    assert all(isinstance(value, int) and 0 <= value <= 100 for value in df.values.flatten())

def test_task_func_start_date_after_end_date():
    with pytest.raises(ValueError):
        task_func("2023-01-10", "2023-01-01", 1)

def test_task_func_zero_num_series():
    with pytest.raises(ValueError):
        task_func("2023-01-01", "2023-01-10", 0)

def test_task_func_negative_num_series():
    with pytest.raises(ValueError):
        task_func("2023-01-01", "2023-01-10", -1)

def test_task_func_with_seed():
    start_date = "2023-01-01"
    end_date = "2023-01-10"
    num_series = 2
    seed = 42
    df1, _ = task_func(start_date, end_date, num_series, seed)
    df2, _ = task_func(start_date, end_date, num_series, seed)
    assert df1.equals(df2)

def test_task_func_plot_return():
    start_date = "2023-01-01"
    end_date = "2023-01-10"
    num_series = 1
    _, ax = task_func(start_date, end_date, num_series)
    assert hasattr(ax, 'get_title') and ax.get_title() == "Random Time Series"
    assert hasattr(ax, 'get_xlabel') and ax.get_xlabel() == "Date"
    assert hasattr(ax, 'get_ylabel') and ax.get_ylabel() == "Value"