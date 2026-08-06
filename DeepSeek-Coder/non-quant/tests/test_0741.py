import pytest
from src_0741 import task_func

def test_task_func():
    # Test case 1: Basic test
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    result = task_func(my_dict)
    assert result == ['c', 'b', 'a']

    # Add more test cases as needed

# Add more test cases as needed