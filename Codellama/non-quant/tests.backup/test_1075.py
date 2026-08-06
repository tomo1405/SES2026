import pytest
from src_1075 import task_func

def test_task_func():
    # Test case 1: Convert time from UTC to EST
    time_string = "12/01/20 12:00:00.000"
    from_tz = "UTC"
    to_tz = "EST"
    expected_result = "12/01/20 08:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 2: Convert time from EST to UTC
    time_string = "12/01/20 12:00:00.000"
    from_tz = "EST"
    to_tz = "UTC"
    expected_result = "12/01/20 16:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 3: Convert time from UTC to PST
    time_string = "12/01/20 12:00:00.000"
    from_tz = "UTC"
    to_tz = "PST"
    expected_result = "12/01/20 05:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 4: Convert time from PST to UTC
    time_string = "12/01/20 12:00:00.000"
    from_tz = "PST"
    to_tz = "UTC"
    expected_result = "12/01/20 20:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 5: Convert time from UTC to IST
    time_string = "12/01/20 12:00:00.000"
    from_tz = "UTC"
    to_tz = "IST"
    expected_result = "12/01/20 17:30:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 6: Convert time from IST to UTC
    time_string = "12/01/20 12:00:00.000"
    from_tz = "IST"
    to_tz = "UTC"
    expected_result = "12/01/20 05:30:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result