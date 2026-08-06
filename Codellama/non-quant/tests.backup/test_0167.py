import pytest
from src_0167 import task_func

def test_task_func_valid_inputs():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    country = 'US'
    business_days = task_func(start_date, end_date, country)
    assert isinstance(business_days, list)
    assert all(isinstance(day, datetime) for day in business_days)

def test_task_func_invalid_inputs():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    country = 'US'
    with pytest.raises(ValueError):
        task_func(start_date, end_date, country, 'invalid_country')
    with pytest.raises(ValueError):
        task_func(start_date, end_date, 'invalid_country')
    with pytest.raises(ValueError):
        task_func(start_date, end_date, country, 'invalid_country')
    with pytest.raises(ValueError):
        task_func(start_date, end_date, 'invalid_country')