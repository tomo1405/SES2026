import pytest
from src_0819 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    text = "Hello, world! This is a test."
    expected_output = ['hello', 'world', 'this', 'is', 'a', 'test']
    assert task_func(text) == expected_output

    # Add more test cases as needed