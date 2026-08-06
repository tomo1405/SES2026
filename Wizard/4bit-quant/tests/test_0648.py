python
import pytz
from dateutil.parser import parse
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
    current_date_in_to_tz = datetime.now(pytz.utc).astimezone(to_tz_obj)

    # Calculate the time difference in seconds
    time_difference = current_date_in_to_tz - given_date_in_to_tz

    return int(time_difference.total_seconds())

def test_task_func():
    # Test case 1: Convert a date from UTC to US/Pacific
    assert task_func('2022-01-01 00:00:00', 'UTC', 'US/Pacific') == 3600

    # Test case 2: Convert a date from US/Pacific to UTC
    assert task_func('2022-07-01 00:00:00', 'US/Pacific', 'UTC') == -25200

    # Test case 3: Convert a date from US/Pacific to US/Eastern
    assert task_func('2022-07-01 00:00:00', 'US/Pacific', 'US/Eastern') == 10800

    # Test case 4: Convert a date from US/Eastern to US/Pacific
    assert task_func('2022-07-01 00:00:00', 'US/Eastern', 'US/Pacific') == -10800

    # Test case 5: Convert a date from US/Eastern to US/Central
    assert task_func('2022-07-01 00:00:00', 'US/Eastern', 'US/Central') == 21600

    # Test case 6: Convert a date from US/Central to US/Eastern
    assert task_func('2022-07-01 00:00:00', 'US/Central', 'US/Eastern') == -21600

    # Test case 7: Convert a date from US/Pacific to US/Mountain
    assert task_func('2022-07-01 00:00:00', 'US/Pacific', 'US/Mountain') == 14400

    # Test case 8: Convert a date from US/Mountain to US/Pacific
    assert task_func('2022-07-01 00:00:00', 'US/Mountain', 'US/Pacific') == -14400

    # Test case 9: Convert a date from US/Pacific to US/Alaska
    assert task_func('2022-07-01 00:00:00', 'US/Pacific', 'US/Alaska') == 32400

    # Test case 10: Convert a date from US/Alaska to US/Pacific
    assert task_func('2022-07-01 00:00:00', 'US/Alaska', 'US/Pacific') == -32400