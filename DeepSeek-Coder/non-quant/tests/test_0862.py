import pytest
from src_0862 import task_func

# Test cases
def test_task_func():
    # Test case 1: Basic functionality
    list_of_lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = task_func(list_of_lists)
    assert len(result) == 3
    assert all(isinstance(basket, Counter) for basket in result)

    # Additional assertions can be added to check the content of the baskets

# You can add more test cases to cover different scenarios