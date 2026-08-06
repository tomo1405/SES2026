import pytest
from src_1013 import task_func


def test_task_func_valid_url():
    url = "https://www.example.com/file.zip"
    filename = "file.zip"
    expected_message = "Download and extraction successful"
    expected_files = ["file1.txt", "file2.txt"]

    message, files = task_func(url, filename)

    assert message == expected_message
    assert files == expected_files


def test_task_func_invalid_url():
    url = "https://www.example.com/file.zip"
    filename = "file.zip"
    expected_message = "Download failed: HTTP status code 404"
    expected_files = []

    message, files = task_func(url, filename)

    assert message == expected_message
    assert files == expected_files


def test_task_func_invalid_zip_file():
    url = "https://www.example.com/file.zip"
    filename = "file.zip"
    expected_message = "Error: Invalid zip file: BadZipFile"
    expected_files = []

    message, files = task_func(url, filename)

    assert message == expected_message
    assert files == expected_files