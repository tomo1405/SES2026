import pytest
from src_0716 import task_func

def test_task_func():
    # Test case 1: Default arguments
    result = task_func()
    assert result == '3.8'

    # Add more test cases as needed