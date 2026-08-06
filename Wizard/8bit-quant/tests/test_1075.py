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
    assert task_func("01/01/2022 12:00:00.000", "UTC", "US/Eastern") == "01/01/2022 07:00:00.000"

    # Test case 2
    assert task_func("01/01/2022 12:00:00.000", "US/Eastern", "UTC") == "01/01/2022 17:00:00.000"

    # Test case 3
    assert task_func("01/01/2022 12:00:00.000", "UTC", "Asia/Kolkata") == "01/01/2022 05:30:00.000"

    # Test case 4
    assert task_func("01/01/2022 12:00:00.000", "Asia/Kolkata", "UTC") == "01/01/2022 19:30:00.000"

    # Test case 5
    assert task_func("01/01/2022 12:00:00.000", "UTC", "Europe/London") == "01/01/2022 06:00:00.000"

    # Test case 6
    assert task_func("01/01/2022 12:00:00.000", "Europe/London", "UTC") == "01/01/2022 18:00:00.000"

    # Test case 7
    assert task_func("01/01/2022 12:00:00.000", "UTC", "Australia/Sydney") == "01/01/2022 10:30:00.000"

    # Test case 8
    assert task_func("01/01/2022 12:00:00.000", "Australia/Sydney", "UTC") == "01/01/2022 22:30:00.000"

    # Test case 9
    assert task_func("01/01/2022 12:00:00.000", "UTC", "Canada/Newfoundland") == "01/01/2022 09:30:00.000"

    # Test case 10
    assert task_func("01/01/2022 12:00:00.000", "Canada/Newfoundland", "UTC") == "01/01/2022 21:30:00.000"