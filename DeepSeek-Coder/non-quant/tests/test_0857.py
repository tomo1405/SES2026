import pytest
from src_0857 import task_func

def test_task_func():
    # Test case 1: Default parameters
    result, _ = task_func()
    assert isinstance(result, tuple), "The result should be a tuple."
    assert len(result) == 2, "The result should contain two elements."

    # Add more test cases as needed

# Add more test cases as needed