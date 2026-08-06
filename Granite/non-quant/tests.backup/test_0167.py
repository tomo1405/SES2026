import pandas as pd
from datetime import datetime
import holidays
import pytest

from src_0167 import task_func

def test_task_func():
    # Test case 1: Check if start_date and end_date are datetime objects
    with pytest.raises(ValueError) as excinfo:
        task_func('2023-01-01', '2023-12-31')
    assert 'start_date and end_date must be datetime objects.' in str(excinfo.value)

    # Test case 2: Check if start_date is not after end_date
    with pytest.raises(ValueError) as excinfo:
        task_func(end_date='2023-01-01', start_date='2023-12-31')
    assert 'start_date must not be after end_date.' in str(excinfo.value)

    # Test case 3: Check if the function returns the expected result
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    country = 'US'
    expected_result = pd.date_range(start_date, end_date)
    expected_result = [date for date in expected_result if date.weekday() < 5 and date not in holidays.CountryHoliday(country)]
    actual_result = task_func(start_date=start_date, end_date=end_date, country=country)
    assert actual_result == expected_result