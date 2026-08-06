import pandas as pd
from datetime import datetime, timedelta
from random import randint, seed as random_seed
from src_0121 import task_func
import pytest

def test_task_func():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    random_seed(seed)
    num_days = (end_date - start_date).days
    expected_dates = pd.Series([start_date + timedelta(days=randint(0, num_days)) for _ in range(num_days)])
    actual_dates = task_func(start_date, end_date, seed)
    assert actual_dates.equals(expected_dates)

def test_task_func_invalid_start_date():
    with pytest.raises(ValueError) as exc_info:
        task_func("invalid start date", datetime(2020, 12, 31), 42)
    assert "start_date and end_date must be datetime.datetime objects." in str(exc_info.value)

def test_task_func_invalid_end_date():
    with pytest.raises(ValueError) as exc_info:
        task_func(datetime(2020, 1, 1), "invalid end date", 42)
    assert "start_date and end_date must be datetime.datetime objects." in str(exc_info.value)

def test_task_func_start_date_later_than_end_date():
    with pytest.raises(ValueError) as exc_info:
        task_func(datetime(2020, 12, 31), datetime(2020, 1, 1), 42)
    assert "start_date must not be later than end_date." in str(exc_info.value)