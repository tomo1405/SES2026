import pytest
from src_0201 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(10, 0.5)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], list)
    assert isinstance(result[1], int)

    # Add more test cases as needed

# Add more test cases as needed