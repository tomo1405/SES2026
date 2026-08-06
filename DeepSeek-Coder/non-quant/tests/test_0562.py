import pytest
from src_0562 import task_func

def test_task_func():
    # Test case 1: Basic conversion
    date_str = "2023-04-01 12:00:00"
    from_tz = 'UTC'
    to_tz = 'US/Eastern'
    expected_output = '2023-04-01 08:00:00'
    assert task_func(date_str, from_tz, to_tz) == expected_output

    # Add more test cases as needed

# Add more test cases as needed