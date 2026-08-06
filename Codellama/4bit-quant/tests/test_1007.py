import pytest
from src_1007 import task_func

def test_task_func_valid_url():
    url = "https://example.com/file.zip"
    download_path = "mnt/data/downloads/"
    expected_extract_path = "mnt/data/downloads/file"

    result = task_func(url, download_path)

    assert result == expected_extract_path

def test_task_func_invalid_url():
    url = "https://example.com/file.txt"
    download_path = "mnt/data/downloads/"

    result = task_func(url, download_path)

    assert result == "Error: The URL does not point to a ZIP file."

def test_task_func_invalid_download_path():
    url = "https://example.com/file.zip"
    download_path = "mnt/data/downloads/invalid"

    result = task_func(url, download_path)

    assert result == "Error: Unable to download the file from the provided URL."

def test_task_func_bad_zip_file():
    url = "https://example.com/file.zip"
    download_path = "mnt/data/downloads/"

    with open(download_path, "wb") as f:
        f.write(b"This is not a valid ZIP file.")

    result = task_func(url, download_path)

    assert result == "Error: The downloaded file is not a valid ZIP file."

def test_task_func_runtime_error():
    url = "https://example.com/file.zip"
    download_path = "mnt/data/downloads/"

    with pytest.raises(RuntimeError):
        task_func(url, download_path)