import pytest
from src_1108 import task_func
from datetime import datetime
import pytz

def test_task_func():
    unix_timestamp = 1631833600
    target_timezone = 'US/Eastern'
    expected_output = '2021-09-17 12:00:00'

    datetime_utc = datetime.utcfromtimestamp(unix_timestamp).replace(tzinfo=pytz.utc)
    datetime_in_target_timezone = datetime_utc.astimezone(pytz.timezone(target_timezone))
    formatted_datetime = datetime_in_target_timezone.strftime(DATE_FORMAT)

    assert task_func(unix_timestamp, target_timezone) == expected_output