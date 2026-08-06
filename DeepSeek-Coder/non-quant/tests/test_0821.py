import pytest
from src_0821 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(3, 5)
    assert len(result) == 3
    assert all(len(word) == 5 for word in result)

    # Add more test cases as needed

# Add more test cases as needed