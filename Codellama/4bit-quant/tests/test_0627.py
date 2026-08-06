import pytest
from src_0627 import task_func

def test_task_func():
    date_str = '2022-01-01 12:00:00'
    from_tz = 'America/New_York'
    expected_date = '2022-01-01 12:00:00'
    expected_tz = 'America/New_York'
    assert task_func(date_str, from_tz) == (expected_date, expected_tz)

    date_str = '2022-01-01 12:00:00'
    from_tz = 'Europe/London'
    expected_date = '2022-01-01 12:00:00'
    expected_tz = 'Europe/London'
    assert task_func(date_str, from_tz) == (expected_date, expected_tz)

    date_str = '2022-01-01 12:00:00'
    from_tz = 'Asia/Shanghai'
    expected_date = '2022-01-01 12:00:00'
    expected_tz = 'Asia/Shanghai'
    assert task_func(date_str, from_tz) == (expected_date, expected_tz)

    date_str = '2022-01-01 12:00:00'
    from_tz = 'Asia/Tokyo'
    expected_date = '2022-01-01 12:00:00'
    expected_tz = 'Asia/Tokyo'
    assert task_func(date_str, from_tz) == (expected_date, expected_tz)

    date_str = '2022-01-01 12:00:00'
    from_tz = 'Australia/Sydney'
    expected_date = '2022-01-01 12:00:00'
    expected_tz = 'Australia/Sydney'
    assert task_func(date_str, from_tz) == (expected_date, expected_tz)