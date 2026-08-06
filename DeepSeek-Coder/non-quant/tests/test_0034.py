import pytest
from src_0034 import task_func

def test_task_func():
    # Test case 1: Basic test
    list_of_pairs = [(1, 2), (3, 4), (5, 6)]
    expected_output = np.array([720])
    assert task_func(list_of_pairs) == expected_output

    # Add more test cases as needed