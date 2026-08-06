import pytest
from src_0932 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    assert task_func("hello") == {'he': 1, 'el': 1, 'll': 1, 'lo': 1}

    # Add more test cases as needed