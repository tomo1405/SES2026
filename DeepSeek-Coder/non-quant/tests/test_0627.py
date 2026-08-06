import pytest
from src_0627 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    date_str = "2023-04-01 12:00:00"
    from_tz = 'UTC'
    expected_output = ('2023-04-01 12:00:00', 'Europe/London')
    assert task_func(date_str, from_tz) == expected_output

    # Add more test cases as needed