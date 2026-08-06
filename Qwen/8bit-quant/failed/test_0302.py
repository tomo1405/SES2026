import pytest
from src_0302 import task_func

def test_task_func_same_timezone():
    date_str = "2023-10-01T12:00:00"
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

def test_task_func_different_timezones():
    date_str = "2023-10-01T12:00:00"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

def test_task_func_solar_cycle_year():
    date_str = "2019-01-01T00:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert result == 1.0  # cos(0) = 1

def test_task_func_solar_activity():
    date_str = "2030-01-01T00:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    expected = math.cos(math.pi * (2030 - 2019) / 11)
    assert math.isclose(result, expected, rel_tol=1e-9)

def test_task_func_invalid_date():
    date_str = "invalid-date"
    from_tz = "UTC"
    to_tz = "UTC"
    with pytest.raises(ValueError):
        task_func(date_str, from_tz, to_tz)

def test_task_func_invalid_timezone():
    date_str = "2023-10-01T12:00:00"
    from_tz = "Invalid/Timezone"
    to_tz = "UTC"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz, to_tz)

    from_tz = "UTC"
    to_tz = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz, to_tz)