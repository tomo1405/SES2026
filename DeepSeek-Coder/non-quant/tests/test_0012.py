import pytest
from src_0012 import task_func

def test_task_func():
    # Test case 1: Basic test
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = (3, 5, 7)
    assert task_func(T1=T1) == expected_output

    # Add more test cases as needed