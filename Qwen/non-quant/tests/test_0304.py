import math

import pytest
import pytz
from src_0304 import task_func


def test_task_func():
    # Test with a date in UTC and convert to Eastern Time
    date_str = "2023-10-01T12:00:00"
    from_tz = "UTC"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

    # Test with a date in Pacific Time and convert to Central Time
    date_str = "2023-10-01T12:00:00"
    from_tz = "America/Los_Angeles"
    to_tz = "America/Chicago"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

    # Test with a date in a different year
    date_str = "1990-01-01T00:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert isinstance(result, float)

    # Test with a date on the exact moon phase year
    date_str = "2015-01-01T00:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert math.isclose(result, 0.0)

    # Test with a date just after the moon phase year
    date_str = "2015-01-02T00:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert result > 0.0

    # Test with a date just before the moon phase year
    date_str = "2014-12-31T23:59:59"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert result < 0.0

    # Test with invalid timezone
    date_str = "2023-10-01T12:00:00"
    from_tz = "UTC"
    to_tz = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz, to_tz)