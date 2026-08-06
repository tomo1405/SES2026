import math

from src_0304 import task_func


def test_task_func():
    # Test with a date in the same year as a moon phase year
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert math.isclose(result, 0, abs_tol=1e-9), f"Expected 0, got {result}"

    # Test with a date in a year between two moon phase years
    date_str = "2018-01-01"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    expected = math.sin(math.pi * 3 / 7)  # 2018 is 3 years after 2015
    assert math.isclose(result, expected, abs_tol=1e-9), f"Expected {expected}, got {result}"

    # Test with a date in a different timezone
    date_str = "2018-01-01T00:00:00+01:00"
    from_tz = "Europe/Berlin"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    expected = math.sin(math.pi * 3 / 7)  # 2018 is 3 years after 2015
    assert math.isclose(result, expected, abs_tol=1e-9), f"Expected {expected}, got {result}"

    # Test with a date in a year before the first moon phase year
    date_str = "1980-01-01"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    expected = math.sin(math.pi * 7 / 7)  # 1980 is 7 years before 1987
    assert math.isclose(result, expected, abs_tol=1e-9), f"Expected {expected}, got {result}"

    # Test with a date in a year after the last moon phase year
    date_str = "2029-01-01"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    expected = math.sin(math.pi * 7 / 7)  # 2029 is 7 years after 2022
    assert math.isclose(result, expected, abs_tol=1e-9), f"Expected {expected}, got {result}"