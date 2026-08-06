from datetime import datetime

import pandas as pd
import pytest
from src_0121 import task_func


def test_task_func_valid_dates():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    result = task_func(start_date, end_date)
    assert isinstance(result, pd.Series)
    assert len(result) == (end_date - start_date).days + 1
    assert all(isinstance(d, datetime) for d in result)

def test_task_func_invalid_start_end_dates():
    with pytest.raises(ValueError, match="start_date and end_date must be datetime.datetime objects."):
        task_func("2020-01-01", datetime(2020, 12, 31))

    with pytest.raises(ValueError, match="start_date and end_date must be datetime.datetime objects."):
        task_func(datetime(2020, 1, 1), "2020-12-31")

    with pytest.raises(ValueError, match="start_date must not be later than end_date."):
        task_func(datetime(2021, 1, 1), datetime(2020, 12, 31))

def test_task_func_same_dates():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 1, 1)
    result = task_func(start_date, end_date)
    assert isinstance(result, pd.Series)
    assert len(result) == 1
    assert result[0] == start_date

def test_task_func_randomness():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    result1 = task_func(start_date, end_date, seed=42)
    result2 = task_func(start_date, end_date, seed=42)
    assert result1.equals(result2)

    result3 = task_func(start_date, end_date, seed=43)
    assert not result1.equals(result3)