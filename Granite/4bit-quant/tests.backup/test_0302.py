import pytest
from src_0302 import task_func

def test_task_func():
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_result = 0.5735761078998913
    result = task_func(date_str, from_tz, to_tz)
    assert result == expected_result

def test_task_func_with_different_input():
    date_str = "2000-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_result = 0.8390715290764512
    result = task_func(date_str, from_tz, to_tz)
    assert result == expected_result

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func("invalid_date_str", "UTC", "US/Eastern")