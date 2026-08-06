import pytest
from src_0958 import task_func

def test_task_func():
    # Test case 1: Basic test
    assert task_func("Hello, World!") == (2, 13, 10)

    # Add more test cases as needed