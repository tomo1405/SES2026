import pytest
from src_0809 import task_func

def test_task_func():
    # Test case 1: Basic test
    text = "This is a test. This test is only a test."
    result = task_func(text)
    assert result.polarity > 0, "Expected positive sentiment"

    # Add more test cases as needed