import math

import pytest
import pytz
from src_0302 import task_func


def test_task_func():
    # Test with a date in the middle of a solar cycle
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

    # Test with a date at the start of a solar cycle
    date_str = "2019-01-01"
    from_tz = "UTC"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    assert math.isclose(result, 1.0, rel_tol=1e-9)

    # Test with a date at the end of a solar cycle
    date_str = "2030-01-01"
    from_tz = "UTC"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    assert math.isclose(result, 1.0, rel_tol=1e-9)

    # Test with a date between two solar cycles
    date_str = "2015-01-01"
    from_tz = "UTC"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    assert math.isclose(result, 0.0, rel_tol=1e-9)

    # Test with a date in a different time zone
    date_str = "2022-01-01"
    from_tz = "Europe/London"
    to_tz = "Asia/Tokyo"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

    # Test with a date that is not a string
    with pytest.raises(ValueError):
        task_func(2022, "UTC", "America/New_York")

    # Test with invalid time zone
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func("2022-01-01", "UTC", "Invalid/TimeZone")