import pytest
from src_0683 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    nested_dict = {
        'a': {'ele': 1, 'b': 2},
        'b': {'ele': 3, 'c': 4}
    }
    expected_output = {'b': math.sin(2), 'c': math.sin(4)}
    assert task_func(nested_dict) == expected_output

    # Add more test cases as needed