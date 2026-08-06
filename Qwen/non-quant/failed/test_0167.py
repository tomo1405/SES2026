import pytest
from src_0167 import task_func
from datetime import datetime

def test_task_func_default_parameters():
    expected_output = task_func(datetime(2023, 1, 1), datetime(2023, 12, 31), 'US')
    assert isinstance(expected_output, list)
    assert all(isinstance(date, datetime) for date in expected_output)

def test_task_func_custom_dates():
    expected_output = task_func(datetime(2023, 1, 1), datetime(2023, 1, 31), 'US')
    assert len(expected_output) == 21  # 21 business days in January 2023

def test_task_func_invalid_start_date_type():
    with pytest.raises(ValueError, match="start_date and end_date must be datetime objects."):
        task_func("2023-01-01", datetime(2023, 12, 31), 'US')

def test_task_func_invalid_end_date_type():
    with pytest.raises(ValueError, match="start_date and end_date must be datetime objects."):
        task_func(datetime(2023, 1, 1), "2023-12-31", 'US')

def test_task_func_start_date_after_end_date():
    with pytest.raises(ValueError, match="start_date must not be after end_date."):
        task_func(datetime(2023, 12, 31), datetime(2023, 1, 1), 'US')

def test_task_func_no_business_days():
    expected_output = task_func(datetime(2023, 12, 25), datetime(2023, 12, 25), 'US')
    assert len(expected_output) == 0  # Christmas is a holiday in the US

def test_task_func_country_holidays():
    expected_output = task_func(datetime(2023, 7, 4), datetime(2023, 7, 4), 'US')
    assert len(expected_output) == 0  # Independence Day is a holiday in the US