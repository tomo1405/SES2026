import pytest
from src_0695 import task_func

def test_task_func():
    # Test case 1: Basic test
    t = [1, 2, 3, 4]
    n = 2
    result = task_func(t, n)
    assert len(result) == 1
    assert result in [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

    # Add more test cases as needed

# Add more test cases as needed