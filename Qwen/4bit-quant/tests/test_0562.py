import pytest
import pytz
from src_0562 import task_func


def test_task_func_valid_timezones():
    assert task_func("2023-10-01 12:00:00", "America/New_York", "Europe/London") == "2023-10-01 17:00:00"

def test_task_func_same_timezone():
    assert task_func("2023-10-01 12:00:00", "America/New_York", "America/New_York") == "2023-10-01 12:00:00"

def test_task_func_invalid_date_format():
    with pytest.raises(ValueError):
        task_func("2023-10-01", "America/New_York", "Europe/London")

def test_task_func_invalid_timezone():
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func("2023-10-01 12:00:00", "Invalid/Timezone", "Europe/London")

def test_task_func_dst_transition():
    # Example of daylight saving time transition
    assert task_func("2023-03-12 02:00:00", "America/New_York", "UTC") == "2023-03-12 07:00:00"
    assert task_func("2023-11-05 01:00:00", "America/New_York", "UTC") == "2023-11-05 06:00:00"