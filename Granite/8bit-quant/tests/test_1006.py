import pytest
from src_1006 import task_func

def test_task_func():
    url = "https://example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"

    # Test if the function returns the expected result when the download and extraction are successful
    result = task_func(url, save_path, extract_path)
    assert result == extract_path

    # Test if the function returns the expected result when the URL is invalid
    url = "https://invalid-url"
    result = task_func(url, save_path, extract_path)
    assert result == f"URL Error: {url} does not exist"

    # Test if the function removes the downloaded zip file if the extraction is successful
    with pytest.raises(FileNotFoundError):
        task_func(url, save_path, extract_path)