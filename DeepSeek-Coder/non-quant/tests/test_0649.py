import pytest
from src_0649 import task_func
from datetime import datetime, timedelta

def test_task_func():
    # Test case 1: Basic case
    date_str = "2023-10-01"
    result = task_func(date_str)
    assert result == datetime(2023, 10, 2)  # 2023-10-02 is a Monday

    # Add more test cases as needed

# Add more test cases as needed