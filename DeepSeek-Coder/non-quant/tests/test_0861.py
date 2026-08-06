import pytest
from src_0861 import task_func

def test_task_func():
    # Test case 1: Basic test
    result = task_func(10, r'[a-z]+', seed=42)
    assert len(result) == 10
    assert all(c.islower() for c in result[0])

    # Add more test cases as needed