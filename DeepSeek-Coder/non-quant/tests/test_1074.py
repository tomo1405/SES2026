import pytest
from src_1074 import task_func

def test_task_func():
    # Test case 1: Normal case
    time_strings = ["01/01/2023 00:00:00.000", "01/01/2023 00:00:01.000"]
    result = task_func(time_strings=time_strings)
    assert result is not None

    # Add more test cases as needed

# Add more test cases as needed