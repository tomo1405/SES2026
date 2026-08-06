import zipfile
from unittest.mock import Mock

import requests
from src_1013 import task_func


def test_task_func():
    url = "https://example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Download and extraction successful", ["file1.txt", "file2.txt"])
    output = task_func(url, filename)
    assert output == expected_output, "Task function output does not match expected output"

def test_task_func_download_failure():
    url = "https://example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Download failed: HTTP status code 404", [])
    response = Mock()
    response.status_code = 404
    task_func.side_effect = requests.exceptions.RequestException(response=response)
    output = task_func(url, filename)
    assert output == expected_output, "Task function output does not match expected output"

def test_task_func_zip_failure():
    url = "https://example.com/file.zip"
    filename = "file.zip"
    expected_output = ("Error: Invalid zip file: BadZipFile('File is not a zip file')", [])
    task_func.side_effect = zipfile.BadZipFile("File is not a zip file")
    output = task_func(url, filename)
    assert output == expected_output, "Task function output does not match expected output"