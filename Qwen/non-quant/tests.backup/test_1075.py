import pytest
from src_1075 import task_func
import pytz
from dateutil.parser import parse

def test_task_func():
    # Test case 1: Convert time from UTC to Eastern Time
    time_string = "01/01/23 12:00:00.000000"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_output = "01/01/23 07:00:00.000000"  # Adjusted for EST (UTC-5)
    assert task_func(time_string, from_tz, to_tz) == expected_output

    # Test case 2: Convert time from Eastern Time to UTC
    time_string = "01/01/23 07:00:00.000000"
    from_tz = "US/Eastern"
    to_tz = "UTC"
    expected_output = "01/01/23 12:00:00.000000"
    assert task_func(time_string, from_tz, to_tz) == expected_output

    # Test case 3: Convert time from UTC to Pacific Time
    time_string = "01/01/23 12:00:00.000000"
    from_tz = "UTC"
    to_tz = "US/Pacific"
    expected_output = "01/01/23 04:00:00.000000"  # Adjusted for PST (UTC-8)
    assert task_func(time_string, from_tz, to_tz) == expected_output

    # Test case 4: Convert time from Pacific Time to UTC
    time_string = "01/01/23 04:00:00.000000"
    from_tz = "US/Pacific"
    to_tz = "UTC"
    expected_output = "01/01/23 12:00:00.000000"
    assert task_func(time_string, from_tz, to_tz) == expected_output

    # Test case 5: Handle daylight saving time conversion
    time_string = "01/03/23 12:00:00.000000"  # DST starts in US/Eastern
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_output = "01/03/23 07:00:00.000000"  # Adjusted for EDT (UTC-4)
    assert task_func(time_string, from_tz, to_tz) == expected_output

    # Test case 6: Handle daylight saving time conversion reverse
    time_string = "01/03/23 07:00:00.000000"  # DST starts in US/Eastern
    from_tz = "US/Eastern"
    to_tz = "UTC"
    expected_output = "01/03/23 12:00:00.000000"
    assert task_func(time_string, from_tz, to_tz) == expected_output