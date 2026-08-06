python
import pytz
import dateutil.parser
import pytest

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_string, from_tz, to_tz):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    dt = dateutil.parser.parse(time_string, dayfirst=True)
    dt = from_zone.localize(dt)
    dt = dt.astimezone(to_zone)

    return dt.strftime(TIME_FORMAT)

def test_task_func():
    # Test case 1
    assert task_func("01/01/2022 00:00:00.000", "UTC", "US/Eastern") == "01/01/2022 05:00:00.000"

    # Test case 2
    assert task_func("01/01/2022 00:00:00.000", "UTC", "US/Pacific") == "01/01/2022 08:00:00.000"

    # Test case 3
    assert task_func("01/01/2022 00:00:00.000", "UTC", "Asia/Tokyo") == "01/01/2022 09:00:00.000"

    # Test case 4
    assert task_func("01/01/2022 00:00:00.000", "US/Eastern", "UTC") == "01/01/2022 00:00:00.000"

    # Test case 5
    assert task_func("01/01/2022 00:00:00.000", "US/Pacific", "UTC") == "01/01/2022 00:00:00.000"

    # Test case 6
    assert task_func("01/01/2022 00:00:00.000", "Asia/Tokyo", "UTC") == "01/01/2022 00:00:00.000"