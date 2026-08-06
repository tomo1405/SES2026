import pytest
from src_0982 import task_func
import pandas as pd
from datetime import datetime
import random

def test_task_func_valid_inputs():
    start_date = "2022-01-01"
    end_date = "2022-01-05"
    num_series = 3
    seed = 42

    df, ax = task_func(start_date, end_date, num_series, seed)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (5, 3)
    assert ax.get_title() == "Random Time Series"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Value"

def test_task_func_invalid_start_date():
    start_date = "2022-01-05"
    end_date = "2022-01-01"
    num_series = 3
    seed = 42

    with pytest.raises(ValueError):
        task_func(start_date, end_date, num_series, seed)

def test_task_func_invalid_num_series():
    start_date = "2022-01-01"
    end_date = "2022-01-05"
    num_series = 0
    seed = 42

    with pytest.raises(ValueError):
        task_func(start_date, end_date, num_series, seed)