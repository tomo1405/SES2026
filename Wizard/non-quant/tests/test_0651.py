python
import pytest
from src_0651 import task_func

def test_task_func():
    # Test case 1: valid input
    assert task_func('2021-01-01 12:00:00', 'US/Pacific') == 3600

    # Test case 2: invalid input (invalid date format)
    with pytest.raises(ValueError):
        task_func('2021-13-01 12:00:00', 'US/Pacific')

    # Test case 3: invalid input (invalid timezone)
    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func('2021-01-01 12:00:00', 'Invalid/Timezone')