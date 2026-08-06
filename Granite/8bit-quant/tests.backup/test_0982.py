import pandas as pd
from datetime import datetime
import random
from src_0982 import task_func
import pytest

def test_task_func():
    start_date = "2022-01-01"
    end_date = "2022-01-31"
    num_series = 3
    seed = 42
    random.seed(seed)
    df, ax = task_func(start_date, end_date, num_series, seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(df.columns) == num_series
    assert df.index[0] == datetime.strptime(start_date, "%Y-%m-%d")
    assert df.index[-1] == datetime.strptime(end_date, "%Y-%m-%d")
    assert ax.get_title() == "Random Time Series"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Value"

def test_task_func_invalid_start_date():
    with pytest.raises(ValueError):
        task_func("2022-02-01", "2022-01-31", 3, 42)

def test_task_func_invalid_num_series():
    with pytest.raises(ValueError):
        task_func("2022-01-01", "2022-01-31", 0, 42)