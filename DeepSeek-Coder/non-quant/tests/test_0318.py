import pytest
from src_0318 import task_func

def test_task_func():
    # Test case 1: Basic test
    example_str = "This is a test string."
    expected_output = {'this': 1.0, 'is': 1.0, 'a': 1.0, 'test': 1.0, 'string': 1.0}
    assert task_func(example_str) == expected_output

    # Add more test cases as needed