import pytest
from src_0304 import task_func

def test_task_func():
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_moon_phase = 0.9999999999999999

    result = task_func(date_str, from_tz, to_tz)

    assert result == expected_moon_phase

def test_task_func_with_different_input():
    date_str = "2020-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_moon_phase = 0.0

    result = task_func(date_str, from_tz, to_tz)

    assert result == expected_moon_phase