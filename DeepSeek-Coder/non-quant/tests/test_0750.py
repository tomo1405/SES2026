import pytest
from src_0750 import task_func

def test_task_func():
    # Test case 1: Normal case
    myList = [1, 2, 3, 4, 5]
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert task_func(myList) == expected_output

    # Add more test cases as needed