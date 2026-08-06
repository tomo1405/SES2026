import pytest
from src_0735 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    content = "This is a simple test case."
    expected_output = {'Noun': 1, 'Verb': 1, 'Adjective': 1}
    assert task_func(content) == expected_output

    # Add more test cases as needed