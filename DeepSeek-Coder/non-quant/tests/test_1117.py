import pytest
from src_1117 import task_func

# Test cases
def test_task_func():
    # Test case 1: Basic functionality
    dict1 = {
        'EMP$$Sales': 5,
        'EMP$$HR': 3,
        'OTHER': 2
    }
    result = task_func(dict1=dict1)
    assert result == (expected_mean, expected_median, expected_mode)

    # Add more test cases as needed

# Add more test cases as needed