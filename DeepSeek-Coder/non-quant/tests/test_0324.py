import pytest
from src_0324 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    text = "apple, apple, banana, banana, orange"
    expected_output = ({'apple': 2, 'banana': 2, 'orange': 1}, [[2.0], [1.0], [1.0]])
    assert task_func(text) == expected_output

    # Add more test cases as needed