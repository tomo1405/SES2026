import pytest
from src_0864 import task_func

def test_task_func():
    # Test case 1: Basic case
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    expected_output = [14, 77]
    assert task_func(list_of_lists) == expected_output

    # Add more test cases as needed