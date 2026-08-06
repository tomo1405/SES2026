import pytest
from src_0366 import task_func

# Test cases
def test_task_func():
    # Test case 1: Basic functionality
    n = 3
    file_name = "output.json"
    result = task_func(n, file_name)
    assert result == file_name

    # Add more test cases as needed

# Add more test cases as needed