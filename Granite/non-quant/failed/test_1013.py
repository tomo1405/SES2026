import pytest
from src_1013 import task_func

def test_task_func():
    url = "https://example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Download and extraction successful", ["file1.txt", "file2.txt"])
    output = task_func(url, filename)
    assert output == expected_output, "Task function returned unexpected output"

def test_task_func_download_failure():
    url = "https://example.com/invalid_file.zip"
    filename = "invalid_file.zip"
    expected_output = ("Download failed: HTTP status code 404", [])
    output = task_func(url, filename)
    assert output == expected_output, "Task function returned unexpected output"

def test_task_func_zip_error():
    url = "https://example.com/invalid_zip_file.zip"
    filename = "invalid_zip_file.zip"
    expected_output = ("Error: Invalid zip file:BadZipFile('File is not a zip file',)", [])
    output = task_func(url, filename)
    assert output == expected_output, "Task function returned unexpected output"