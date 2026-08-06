python
import pytest
from src_1108 import task_func

# Constants
UNIX_TIMESTAMP = 1625232400
TARGET_TIMEZONE = 'US/Pacific'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def test_task_func():
    # Test the function with a valid input
    formatted_datetime = task_func(UNIX_TIMESTAMP, TARGET_TIMEZONE)
    assert formatted_datetime == '2021-07-06 15:00:00'

    # Test the function with an invalid input (non-integer Unix timestamp)
    with pytest.raises(TypeError):
        task_func('not an integer', TARGET_TIMEZONE)

    # Test the function with an invalid input (invalid timezone)
    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(UNIX_TIMESTAMP, 'not a valid timezone')