import pytest
from src_0868 import task_func

def test_task_func():
    # Test case 1
    text1 = "Hello, world!"
    text2 = "This is a test."
    expected_output = ('Hello world', 'This is a test')
    assert task_func(text1, text2) == expected_output

    # Add more test cases as needed