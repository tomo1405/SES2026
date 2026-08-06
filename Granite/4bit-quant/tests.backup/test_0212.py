import pytest
from src_0212 import task_func

def test_task_func():
    url = "https://example.com/file.zip"
    destination_directory = "/path/to/destination"
    headers = {
        'accept': 'application/octet-stream'
    }
    extracted_files = task_func(url, destination_directory, headers)
    assert extracted_files  # Assert that extracted_files is not empty

def test_task_func_with_no_headers():
    url = "https://example.com/file.zip"
    destination_directory = "/path/to/destination"
    extracted_files = task_func(url, destination_directory)
    assert extracted_files  # Assert that extracted_files is not empty