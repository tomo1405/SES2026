import pytest
from src_1013 import task_func

def test_task_func():
    url = "https://example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Download and extraction successful", ["file1.txt", "file2.txt", "file3.txt"])
    output = task_func(url, filename)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_download_failure():
    url = "https://example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Download failed: HTTP status code 404", [])
    response = MockResponse(status_code=404)
    with patch("requests.get", return_value=response):
        output = task_func(url, filename)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_zip_failure():
    url = "https://example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Error: Invalid zip file: Password required", [])
    with patch("zipfile.ZipFile.extractall", side_effect=zipfile.BadZipFile("Password required")):
        output = task_func(url, filename)
    assert output == expected_output, "Output does not match expected output"

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code