python
import pytest
from src_0651 import task_func

def test_task_func():
    # Test case 1: valid input
    assert task_func('2022-01-01 12:00:00', 'US/Eastern') == 31536000

    # Test case 2: invalid input (invalid date string)
    with pytest.raises(ValueError):
        task_func('2022-01-32 12:00:00', 'US/Eastern')

    # Test case 3: invalid input (invalid timezone string)
    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func('2022-01-01 12:00:00', 'invalid_timezone')