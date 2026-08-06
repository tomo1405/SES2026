import pytest
from src_0304 import task_func

def test_task_func():
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "America/New_York"
    expected_moon_phase = 0.9999999999999999

    moon_phase = task_func(date_str, from_tz, to_tz)

    assert moon_phase == expected_moon_phase