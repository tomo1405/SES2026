import pytest
from src_0304 import task_func

def test_task_func_with_same_timezone():
    date_str = "2023-10-01T12:00:00"
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

def test_task_func_with_different_timezones():
    date_str = "2023-10-01T12:00:00"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

def test_task_func_with_edge_year():
    date_str = "1987-01-01T00:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert result == math.sin(0)

def test_task_func_with_intermediate_year():
    date_str = "2004-06-15T00:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    expected_moon_phase_year = 2001
    years_since_moon_phase_year = abs(2004 - expected_moon_phase_year)
    expected_moon_phase = math.sin(math.pi * years_since_moon_phase_year / 7)
    assert math.isclose(result, expected_moon_phase)

def test_task_func_with_future_year():
    date_str = "2030-01-01T00:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    expected_moon_phase_year = 2022
    years_since_moon_phase_year = abs(2030 - expected_moon_phase_year)
    expected_moon_phase = math.sin(math.pi * years_since_moon_phase_year / 7)
    assert math.isclose(result, expected_moon_phase)