import pytest
from src_0167 import task_func
from datetime import datetime
import holidays

def test_task_func_default_parameters():
    result = task_func()
    assert len(result) > 0, "The result should contain some business days."
    assert all(isinstance(date, datetime) for date in result), "All elements in the result should be datetime objects."

def test_task_func_custom_dates():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 31)
    result = task_func(start_date, end_date)
    assert len(result) == 21, "There should be 21 business days between January 1, 2023, and January 31, 2023."

def test_task_func_no_business_days():
    start_date = datetime(2023, 12, 24)
    end_date = datetime(2023, 12, 30)
    result = task_func(start_date, end_date)
    assert len(result) == 0, "There should be no business days between December 24, 2023, and December 30, 2023."

def test_task_func_invalid_start_end_dates():
    with pytest.raises(ValueError, match="start_date must not be after end_date."):
        task_func(datetime(2023, 12, 31), datetime(2023, 1, 1))

def test_task_func_invalid_date_types():
    with pytest.raises(ValueError, match="start_date and end_date must be datetime objects."):
        task_func("2023-01-01", datetime(2023, 12, 31))
    with pytest.raises(ValueError, match="start_date and end_date must be datetime objects."):
        task_func(datetime(2023, 1, 1), "2023-12-31")

def test_task_func_non_us_country():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    result = task_func(start_date, end_date, country='CA')
    assert len(result) > 0, "The result should contain some business days for Canada."
    assert all(isinstance(date, datetime) for date in result), "All elements in the result should be datetime objects."