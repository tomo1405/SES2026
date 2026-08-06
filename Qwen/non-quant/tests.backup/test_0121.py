import pytest
from src_0121 import task_func
from datetime import datetime

def test_task_func_default_parameters():
    result = task_func()
    assert isinstance(result, pd.Series)
    assert len(result) == 365
    assert all(isinstance(date, datetime) for date in result)

def test_task_func_custom_dates():
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 1, 31)
    result = task_func(start_date, end_date)
    assert isinstance(result, pd.Series)
    assert len(result) == 31
    assert all(isinstance(date, datetime) for date in result)
    assert all(start_date <= date <= end_date for date in result)

def test_task_func_invalid_start_date_type():
    with pytest.raises(ValueError):
        task_func(start_date="2020-01-01", end_date=datetime(2020, 12, 31))

def test_task_func_invalid_end_date_type():
    with pytest.raises(ValueError):
        task_func(start_date=datetime(2020, 1, 1), end_date="2020-12-31")

def test_task_func_start_date_after_end_date():
    with pytest.raises(ValueError):
        task_func(start_date=datetime(2020, 12, 31), end_date=datetime(2020, 1, 1))

def test_task_func_same_start_and_end_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 1, 1)
    result = task_func(start_date, end_date)
    assert isinstance(result, pd.Series)
    assert len(result) == 1
    assert result[0] == start_date

def test_task_func_with_custom_seed():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 1, 31)
    result1 = task_func(start_date, end_date, seed=123)
    result2 = task_func(start_date, end_date, seed=123)
    assert result1.equals(result2)