import pytest
from src_0562 import task_func

def test_task_func():
    date_str = '2023-01-01 12:00:00'
    from_tz = 'UTC'
    to_tz = 'US/Eastern'
    expected_output = '2023-01-01 06:00:00'

    output = task_func(date_str, from_tz, to_tz)

    assert output == expected_output