import pytest
from src_0248 import task_func

def test_task_func():
    # Test case 1: Default parameters
    result = task_func()
    assert len(result) == 5000
    assert all(0 <= value <= 10 for value in result['Normalized Value'])

    # Add more test cases as needed

# Add more test cases as needed