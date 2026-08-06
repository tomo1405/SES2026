python
import pytest
from src_1013 import task_func

def test_task_func():
    # Test case 1
    url = "https://www.example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Download and extraction successful", ["file1.txt", "file2.txt"])
    assert task_func(url, filename) == expected_output

    # Test case 2
    url = "https://www.example.com/invalid.zip"
    filename = "invalid.zip"
    expected_output = ("Error: Invalid zip file: File is not a zip file", [])
    assert task_func(url, filename) == expected_output

    # Test case 3
    url = "https://www.example.com/timeout.zip"
    filename = "timeout.zip"
    expected_output = ("Error: Timeout", [])
    assert task_func(url, filename) == expected_output

    # Test case 4
    url = "https://www.example.com/error.zip"
    filename = "error.zip"
    expected_output = ("Error: Error", [])
    assert task_func(url, filename) == expected_output