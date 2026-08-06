import pytest
from src_0033 import task_func

def test_task_func():
    # Test case 1: Valid URL with a valid tag
    url = "https://example.com"
    tag = "title"
    expected_output = "Example Domain"
    assert task_func(url, tag) == expected_output

    # Add more test cases as needed