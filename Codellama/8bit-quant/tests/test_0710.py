import pytest
from src_0710 import task_func

def test_task_func():
    # Test case 1: Valid input
    raw_string = "SGVsbG8gV29ybGQh"
    line_length = 10
    expected_output = "Hello World!"
    assert task_func(raw_string, line_length) == expected_output

    # Test case 2: Invalid input
    raw_string = "Invalid input"
    line_length = 10
    with pytest.raises(ValueError):
        task_func(raw_string, line_length)

    # Test case 3: Empty input
    raw_string = ""
    line_length = 10
    expected_output = ""
    assert task_func(raw_string, line_length) == expected_output

    # Test case 4: Line length is 0
    raw_string = "SGVsbG8gV29ybGQh"
    line_length = 0
    expected_output = "SGVsbG8gV29ybGQh"
    assert task_func(raw_string, line_length) == expected_output

    # Test case 5: Line length is negative
    raw_string = "SGVsbG8gV29ybGQh"
    line_length = -10
    with pytest.raises(ValueError):
        task_func(raw_string, line_length)