import pytest
from src_0736 import task_func

def test_task_func():
    # Test case 1: Basic test
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = {'mean': 5.0, 'variance': 6.666666666666667}
    assert task_func(L) == expected

    # Add more test cases as needed

# You can add more test cases to cover different scenarios