import pytest
from src_1099 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    text = "This is a test. This test is only a test."
    top_n = 2
    expected_output = [('test', 2), ('is', 1), ('a', 1)]
    assert task_func(text, top_n) == expected_output

    # Add more test cases as needed