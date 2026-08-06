python
import pytz
from dateutil import parser
import pytest

def task_func(date_str, from_tz, to_tz):
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    date = parser.parse(date_str).replace(tzinfo=from_tz)
    date = date.astimezone(to_tz)

    return date.strftime('%Y-%m-%d %H:%M:%S')

def test_task_func():
    # Test case 1
    assert task_func('2022-01-01 12:00:00', 'US/Pacific', 'US/Eastern') == '2022-01-01 06:00:00'

    # Test case 2
    assert task_func('2022-07-01 12:00:00', 'US/Pacific', 'US/Eastern') == '2022-07-01 05:00:00'

    # Test case 3
    assert task_func('2022-12-31 12:00:00', 'US/Pacific', 'US/Eastern') == '2022-12-31 05:00:00'

    # Test case 4
    assert task_func('2022-01-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2021-12-31 23:00:00'

    # Test case 5
    assert task_func('2022-07-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-06-30 22:00:00'

    # Test case 6
    assert task_func('2022-12-31 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-12-30 22:00:00'