python
import pandas as pd
from datetime import datetime
import random
import pytest

def task_func(start_date, end_date, num_series, seed=None):
    if seed is not None:
        random.seed(seed)

    start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
    if start_date_dt > end_date_dt:
        raise ValueError("start_date must be earlier than or equal to end_date.")
    if num_series < 1:
        raise ValueError("num_series must be at least 1.")

    date_range = pd.date_range(start_date_dt, end_date_dt)

    data = {}
    for i in range(num_series):
        series_name = f"series_{i+1}"
        data[series_name] = [random.randint(0, 100) for _ in range(len(date_range))]

    df = pd.DataFrame(data, index=date_range)

    ax = df.plot()
    ax.set_title("Random Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")

    return df, ax

def test_task_func():
    # Test case 1: valid input
    df, ax = task_func("2021-01-01", "2021-01-31", 3, seed=42)
    assert df.shape == (31, 3)
    assert ax.get_title() == "Random Time Series"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Value"

    # Test case 2: invalid input (start_date > end_date)
    with pytest.raises(ValueError):
        task_func("2021-01-31", "2021-01-01", 3)

    # Test case 3: invalid input (num_series < 1)
    with pytest.raises(ValueError):
        task_func("2021-01-01", "2021-01-31", 0)