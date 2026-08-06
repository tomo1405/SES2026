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
    assert task_func('2022-01-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-01-01 07:00:00'

    # Test case 2
    assert task_func('2022-07-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-07-01 08:00:00'

    # Test case 3
    assert task_func('2022-12-31 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-12-31 08:00:00'

    # Test case 4
    assert task_func('2022-02-28 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-02-28 07:00:00'

    # Test case 5
    assert task_func('2022-02-29 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-02-29 07:00:00'

    # Test case 6
    assert task_func('2022-03-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-03-01 08:00:00'

    # Test case 7
    assert task_func('2022-03-31 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-03-31 08:00:00'

    # Test case 8
    assert task_func('2022-04-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-04-01 08:00:00'

    # Test case 9
    assert task_func('2022-04-30 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-04-30 08:00:00'

    # Test case 10
    assert task_func('2022-05-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-05-01 08:00:00'

    # Test case 11
    assert task_func('2022-05-31 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-05-31 08:00:00'

    # Test case 12
    assert task_func('2022-06-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-06-01 08:00:00'

    # Test case 13
    assert task_func('2022-06-30 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-06-30 08:00:00'

    # Test case 14
    assert task_func('2022-07-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-07-01 08:00:00'

    # Test case 15
    assert task_func('2022-07-31 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-07-31 08:00:00'

    # Test case 16
    assert task_func('2022-08-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-08-01 08:00:00'

    # Test case 17
    assert task_func('2022-08-31 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-08-31 08:00:00'

    # Test case 18
    assert task_func('2022-09-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-09-01 08:00:00'

    # Test case 19
    assert task_func('2022-09-30 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-09-30 08:00:00'

    # Test case 20
    assert task_func('2022-10-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-10-01 08:00:00'

    # Test case 21
    assert task_func('2022-10-31 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-10-31 08:00:00'

    # Test case 22
    assert task_func('2022-11-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-11-01 08:00:00'

    # Test case 23
    assert task_func('2022-11-30 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-11-30 08:00:00'

    # Test case 24
    assert task_func('2022-12-01 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-12-01 08:00:00'

    # Test case 25
    assert task_func('2022-12-31 12:00:00', 'US/Eastern', 'US/Pacific') == '2022-12-31 08:00:00'