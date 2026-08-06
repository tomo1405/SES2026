import pytest
from src_0562 import task_func

def test_task_func():
    date_str = '2022-01-01 12:00:00'
    from_tz = 'UTC'
    to_tz = 'America/New_York'
    expected_result = '2022-01-01 06:00:00'

    result = task_func(date_str, from_tz, to_tz)

    assert result == expected_result