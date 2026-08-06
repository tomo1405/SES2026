import pytest
from src_1095 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    text = "$$$hello $world $$$"
    expected_output = [('$$$', 1)]
    assert task_func(text) == expected_output

    # Add more test cases as needed