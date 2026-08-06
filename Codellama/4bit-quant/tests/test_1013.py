import pytest
from src_1013 import task_func

def test_task_func():
    # Test with valid URL and filename
    url = "https://www.example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Download and extraction successful", ["file1.txt", "file2.txt"])
    assert task_func(url, filename) == expected_output

    # Test with invalid URL
    url = "https://www.example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Download failed: HTTP status code 404", [])
    assert task_func(url, filename) == expected_output

    # Test with invalid filename
    url = "https://www.example.com/file.zip"
    filename = "file.txt"
    expected_output = ("Error: Invalid zip file: Not a zip file", [])
    assert task_func(url, filename) == expected_output

    # Test with invalid URL and filename
    url = "https://www.example.com/file.zip"
    filename = "file.txt"
    expected_output = ("Error: Invalid zip file: Not a zip file", [])
    assert task_func(url, filename) == expected_output