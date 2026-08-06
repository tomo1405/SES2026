import pytest
from src_1075 import task_func

@pytest.mark.parametrize("time_string, from_tz, to_tz, expected", [
    ("12/01/18 12:00:00.000", "UTC", "US/Eastern", "12/01/18 08:00:00.000"),
    ("12/01/18 12:00:00.000", "UTC", "US/Central", "12/01/18 09:00:00.000"),
    ("12/01/18 12:00:00.000", "UTC", "US/Mountain", "12/01/18 10:00:00.000"),
    ("12/01/18 12:00:00.000", "UTC", "US/Pacific", "12/01/18 11:00:00.000"),
    ("12/01/18 12:00:00.000", "UTC", "US/Alaska", "12/01/18 09:00:00.000"),
    ("12/01/18 12:00:00.000", "UTC", "US/Hawaii", "12/01/18 10:00:00.000"),
])
def test_task_func(time_string, from_tz, to_tz, expected):
    assert task_func(time_string, from_tz, to_tz) == expected