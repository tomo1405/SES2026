import pytest
from src_1103 import task_func

def test_task_func():
    # Test case 1: Valid script path
    result = task_func("/path/to/script.R")
    assert "Start Time" in result
    assert "End Time" in result
    assert "Stdout" in result
    assert "Stderr" in result

    # Add more test cases as needed