import pytest
from src_0710 import task_func

def test_task_func():
    # Test case 1
    raw_string = "SGVsbG8gV29ybGQh"
    line_length = 10
    expected_output = "Hello World!"
    assert task_func(raw_string, line_length) == expected_output

    # Add more test cases as needed