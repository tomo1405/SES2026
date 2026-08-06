import pytest
from src_1073 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = [
        pd.Series([3, 2, 1], index=[1, 2, 3]),
        pd.Series([3, 2, 1], index=[4, 5, 6]),
        pd.Series([3, 2, 1], index=[7, 8, 9])
    ]
    assert task_func(list_of_lists) == expected_output

    # Add more test cases as needed

# You can add more test cases to cover different scenarios