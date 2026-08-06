python
import pytz
from dateutil.parser import parse
import datetime
import pytest

def task_func(date_str, from_tz, to_tz):
    # Get timezone objects for the source and destination timezones
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)

    # Parse the given date string and localize it to the source timezone
    given_date_naive = parse(date_str)
    given_date = from_tz_obj.localize(given_date_naive)

    # Convert the given date to the destination timezone
    given_date_in_to_tz = given_date.astimezone(to_tz_obj)

    # Get the current time in the destination timezone
    current_date_in_to_tz = datetime.datetime.now(pytz.utc).astimezone(to_tz_obj)

    # Calculate the time difference in seconds
    time_difference = current_date_in_to_tz - given_date_in_to_tz

    return int(time_difference.total_seconds())

def test_task_func():
    # Test case 1: Valid input
    assert task_func('2022-01-01 12:00:00', 'US/Pacific', 'US/Eastern') == 25200

    # Test case 2: Invalid input (invalid date string)
    with pytest.raises(ValueError):
        task_func('2022-01-32 12:00:00', 'US/Pacific', 'US/Eastern')

    # Test case 3: Invalid input (invalid timezone)
    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func('2022-01-01 12:00:00', 'US/Pacific', 'Invalid/Timezone')