import pytest
from src_1131 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func("test_directory")
    assert result == "test_directory/hashes.json"

    # Add more test cases as needed