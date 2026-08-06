python
import pytest
from src_1108 import task_func

# Constants
UNIX_TIMESTAMP = 1625232000
TARGET_TIMEZONE = 'US/Pacific'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def test_task_func():
    # Test with a valid Unix timestamp and target timezone
    formatted_datetime = task_func(UNIX_TIMESTAMP, TARGET_TIMEZONE)
    assert formatted_datetime == '2021-07-01 00:00:00'

    # Test with a Unix timestamp that is too small
    with pytest.raises(ValueError):
        task_func(-1, TARGET_TIMEZONE)

    # Test with a Unix timestamp that is too large
    with pytest.raises(ValueError):
        task_func(2**31, TARGET_TIMEZONE)

    # Test with an invalid target timezone
    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(UNIX_TIMESTAMP, 'invalid_timezone')