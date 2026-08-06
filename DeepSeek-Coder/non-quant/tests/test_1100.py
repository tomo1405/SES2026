import pytest
from src_1100 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    text = "Hello, world! This is a test. This test is to check the function."
    expected_output = [('hello', 1), ('world', 1), ('this', 2), ('is', 2), ('test', 2), ('a', 1), ('to', 1), ('check', 1), ('the', 1), ('function', 1)]
    assert task_func(text) == expected_output

    # Add more test cases as needed