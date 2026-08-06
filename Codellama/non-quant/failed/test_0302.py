import pytest
from src_0302 import task_func

def test_task_func():
    date_str = "2019-01-01"
    from_tz = "UTC"
    to_tz = "America/New_York"
    expected_solar_activity = 0.7071067811865476

    solar_activity = task_func(date_str, from_tz, to_tz)

    assert solar_activity == expected_solar_activity