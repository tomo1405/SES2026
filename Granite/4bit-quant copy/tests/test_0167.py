import pandas as pd
from datetime import datetime
import holidays
import pytest

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects.")
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date.")

    country_holidays = holidays.CountryHoliday(country)
    dates = pd.date_range(start_date, end_date)
    business_days = [date for date in dates if date.weekday() < 5 and date not in country_holidays]

    return business_days

def test_task_func():
    # Test case 1: Check if start_date and end_date are datetime objects
    with pytest.raises(ValueError) as excinfo:
        task_func(start_date='2023-01-01', end_date='2023-12-31')
    assert "start_date and end_date must be datetime objects." in str(excinfo.value)

    # Test case 2: Check if start_date is not after end_date
    with pytest.raises(ValueError) as excinfo:
        task_func(start_date=datetime(2023, 12, 31), end_date=datetime(2023, 1, 1))
    assert "start_date must not be after end_date." in str(excinfo.value)

    # Test case 3: Check if the function returns the expected result
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    country = 'US'
    expected_result = pd.date_range(start_date, end_date)
    actual_result = task_func(start_date=start_date, end_date=end_date, country=country)
    assert actual_result == expected_result.tolist()