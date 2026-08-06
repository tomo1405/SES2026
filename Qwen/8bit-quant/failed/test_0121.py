import pytest
from src_0121 import task_func
from datetime import datetime

def test_task_func_with_default_parameters():
    result = task_func()
    assert isinstance(result, pd.Series)
    assert len(result) == 365
    assert result.dt.date.min() >= datetime(2020, 1, 1).date()
    assert result.dt.date.max() <= datetime(2020, 12, 31).date()

def test_task_func_with_custom_dates():
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 1, 31)
    result = task_func(start_date=start_date, end_date=end_date)
    assert isinstance(result, pd.Series)
    assert len(result) == 31
    assert result.dt.date.min() >= start_date.date()
    assert result.dt.date.max() <= end_date.date()

def test_task_func_with_invalid_start_date_type():
    with pytest.raises(ValueError):
        task_func(start_date="2020-01-01")

def test_task_func_with_invalid_end_date_type():
    with pytest.raises(ValueError):
        task_func(end_date="2020-12-31")

def test_task_func_with_start_date_after_end_date():
    with pytest.raises(ValueError):
        task_func(start_date=datetime(2020, 12, 31), end_date=datetime(2020, 1, 1))

def test_task_func_with_same_start_and_end_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 1, 1)
    result = task_func(start_date=start_date, end_date=end_date)
    assert isinstance(result, pd.Series)
    assert len(result) == 1
    assert result.iloc[0].date() == start_date.date()