import pytest
from src_0794 import task_func

def test_task_func():
    # Test case 1: Default behavior
    result = task_func()
    assert len(result) == 10
    assert all(isinstance(x, str) for x in result)

    # Add more test cases as needed