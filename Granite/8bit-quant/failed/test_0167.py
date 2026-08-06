import pandas as pd
from datetime import datetime
import holidays
from src_0167 import task_func
import pytest

def test_task_func_valid_input():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    country = 'US'
    result = task_func(start_date, end_date, country)
    assert isinstance(result, list)
    assert all(isinstance(date, datetime) for date in result)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func('2023-01-01', '2023-12-31', 'US')
    with pytest.raises(ValueError):
        task_func(datetime(2023, 1, 1), datetime(2023, 1, 1), 'US')
    with pytest.raises(ValueError):
        task_func(datetime(2023, 1, 1), datetime(2023, 1, 1), 123)

def test_task_func_holidays():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    country = 'US'
    result = task_func(start_date, end_date, country)
    country_holidays = holidays.CountryHoliday(country)
    dates = pd.date_range(start_date, end_date)
    expected_result = [date for date in dates if date.weekday() < 5 and date not in country_holidays]
    assert result == expected_result