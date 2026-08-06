import pytest
from src_0562 import task_func

def test_task_func():
    # Test converting from UTC to EST
    date_str = "2023-10-15 12:00:00"
    from_tz = "UTC"
    to_tz = "America/New_York"
    expected_output = "2023-10-15 07:00:00"
    assert task_func(date_str, from_tz, to_tz) == expected_output

    # Test converting from EST to UTC
    date_str = "2023-10-15 07:00:00"
    from_tz = "America/New_York"
    to_tz = "UTC"
    expected_output = "2023-10-15 12:00:00"
    assert task_func(date_str, from_tz, to_tz) == expected_output

    # Test converting from JST to PST
    date_str = "2023-10-15 12:00:00"
    from_tz = "Asia/Tokyo"
    to_tz = "America/Los_Angeles"
    expected_output = "2023-10-14 19:00:00"
    assert task_func(date_str, from_tz, to_tz) == expected_output

    # Test with daylight saving time (EST to EDT)
    date_str = "2023-03-12 01:00:00"
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    expected_output = "2023-03-12 02:00:00"
    assert task_func(date_str, from_tz, to_tz) == expected_output

    # Test with daylight saving time (EDT to EST)
    date_str = "2023-11-05 01:00:00"
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    expected_output = "2023-11-05 00:00:00"
    assert task_func(date_str, from_tz, to_tz) == expected_output