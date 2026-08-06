import pytest
from src_0938 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    input_str = "Hello, World!"
    expected_output = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    assert task_func(input_str) == expected_output

    # Add more test cases as needed

# Add more test cases as needed