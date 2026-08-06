import pytest
from src_0941 import task_func

def test_task_func():
    # Test case 1
    input_str = "Hello, world! This is a test."
    expected_output = {'Hello': 1, 'world': 1, 'This': 1, 'is': 1, 'a': 1, 'test': 1}
    assert task_func(input_str) == expected_output

    # Add more test cases as needed