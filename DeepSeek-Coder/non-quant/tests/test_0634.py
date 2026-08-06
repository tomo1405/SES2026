import pytest
from src_0634 import task_func

def test_task_func():
    # Test case 1
    text = "This is a test. This test is only a test."
    expected_output = {'this': 2, 'is': 2, 'a': 2, 'test': 2}
    assert task_func(text) == expected_output

    # Add more test cases as needed