import pytest
from src_0331 import task_func

def test_task_func():
    # Test case 1: Basic test
    result = task_func(10, 3)
    assert len(result[1]) == 3
    assert all(x in result[0] for x in result[1])

    # Add more test cases as needed