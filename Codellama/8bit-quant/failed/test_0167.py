import pytest
from src_0167 import task_func

def test_task_func_valid_input():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    country = 'US'
    expected_output = [datetime(2023, 1, 3), datetime(2023, 1, 4), datetime(2023, 1, 5), ...]
    assert task_func(start_date, end_date, country) == expected_output

def test_task_func_invalid_input():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    country = 'US'
    with pytest.raises(ValueError):
        task_func(start_date, end_date, country)