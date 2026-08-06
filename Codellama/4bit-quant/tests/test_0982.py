from datetime import datetime

import pytest
from src_0982 import task_func


def test_task_func():
    # Test case 1: start_date is earlier than end_date
    start_date = "2022-01-01"
    end_date = "2022-01-02"
    num_series = 1
    seed = 123
    df, ax = task_func(start_date, end_date, num_series, seed)
    assert df.index[0] == datetime.strptime(start_date, "%Y-%m-%d")
    assert df.index[-1] == datetime.strptime(end_date, "%Y-%m-%d")
    assert len(df.columns) == num_series
    assert len(df) == len(df.index)
    assert ax.get_title() == "Random Time Series"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Value"

    # Test case 2: start_date is later than end_date
    start_date = "2022-01-02"
    end_date = "2022-01-01"
    num_series = 1
    seed = 123
    with pytest.raises(ValueError):
        task_func(start_date, end_date, num_series, seed)

    # Test case 3: num_series is less than 1
    start_date = "2022-01-01"
    end_date = "2022-01-02"
    num_series = 0
    seed = 123
    with pytest.raises(ValueError):
        task_func(start_date, end_date, num_series, seed)

    # Test case 4: seed is not None
    start_date = "2022-01-01"
    end_date = "2022-01-02"
    num_series = 1
    seed = 123
    df, ax = task_func(start_date, end_date, num_series, seed)
    assert df.index[0] == datetime.strptime(start_date, "%Y-%m-%d")
    assert df.index[-1] == datetime.strptime(end_date, "%Y-%m-%d")
    assert len(df.columns) == num_series
    assert len(df) == len(df.index)
    assert ax.get_title() == "Random Time Series"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Value"