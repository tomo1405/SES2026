import pytest
from src_1090 import task_func

def test_task_func():
    # Test case 1
    list_of_tuples = [(1, 'A'), (2, 'B'), (3, 'A'), (4, 'B')]
    expected_output = (10, {'A': 2, 'B': 2})
    assert task_func(list_of_tuples) == expected_output

    # Add more test cases as needed