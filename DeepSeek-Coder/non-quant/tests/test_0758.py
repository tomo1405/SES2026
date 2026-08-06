import pytest
from src_0758 import task_func

def test_task_func():
    # Test case 1: Basic test
    arr = ["192.168.1.1", "10.0.0.1"]
    expected_output = ["1.1.1.192", "1.1.0.10"]
    assert task_func(arr) == expected_output

    # Add more test cases as needed