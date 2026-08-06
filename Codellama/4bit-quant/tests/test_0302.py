import pytest
from src_0302 import task_func

@pytest.mark.parametrize("date_str, from_tz, to_tz, expected_solar_activity", [
    ("2019-01-01", "UTC", "UTC", 0.9999999999999999),
    ("2019-01-01", "UTC", "America/New_York", 0.9999999999999999),
    ("2019-01-01", "UTC", "Asia/Tokyo", 0.9999999999999999),
    ("2019-01-01", "UTC", "Europe/London", 0.9999999999999999),
    ("2019-01-01", "UTC", "Australia/Sydney", 0.9999999999999999),
])
def test_task_func(date_str, from_tz, to_tz, expected_solar_activity):
    solar_activity = task_func(date_str, from_tz, to_tz)
    assert solar_activity == expected_solar_activity