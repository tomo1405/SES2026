import pytest
from src_1108 import task_func
from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def test_task_func():
    unix_timestamp = 1632304000
    target_timezone = 'America/New_York'
    expected_output = '2021-09-22 19:00:00'

    result = task_func(unix_timestamp, target_timezone)
    assert result == expected_output

def test_task_func_invalid_timestamp():
    unix_timestamp = 'invalid'
    target_timezone = 'America/New_York'

    with pytest.raises(TypeError):
        task_func(unix_timestamp, target_timezone)

def test_task_func_invalid_timezone():
    unix_timestamp = 1632304000
    target_timezone = 'invalid'

    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(unix_timestamp, target_timezone)