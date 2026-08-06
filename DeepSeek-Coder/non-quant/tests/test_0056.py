import pytest
from src_0056 import task_func

def test_task_func():
    # Test case 1
    text = "This is a test. This test is only a test."
    expected_output = {
        "Sentence 1": 4,
        "Sentence 2": 4
    }
    assert task_func(text) == expected_output

    # Add more test cases as needed