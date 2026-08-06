python
import pytest
from src_1013 import task_func

# Constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

def test_task_func():
    # Test case 1: Download and extract a valid zip file
    url = "https://www.example.com/example.zip"
    filename = "example.zip"
    expected_output = ("Download and extraction successful", ["example.txt"])
    actual_output = task_func(url, filename)
    assert actual_output == expected_output

    # Test case 2: Download a non-existent file
    url = "https://www.example.com/nonexistent.zip"
    filename = "nonexistent.zip"
    expected_output = ("Download failed: HTTP status code 404", [])
    actual_output = task_func(url, filename)
    assert actual_output == expected_output

    # Test case 3: Download a file with an invalid zip file
    url = "https://www.example.com/invalid.zip"
    filename = "invalid.zip"
    expected_output = ("Error: Invalid zip file: File is not a zip file", [])
    actual_output = task_func(url, filename)
    assert actual_output == expected_output

    # Test case 4: Download a file with a timeout error
    url = "https://www.example.com/timeout.zip"
    filename = "timeout.zip"
    expected_output = ("Error: Max retries exceeded with url: /timeout.zip", [])
    actual_output = task_func(url, filename)
    assert actual_output == expected_output