import pytest
from src_1006 import task_func

def test_task_func():
    url = "https://example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"

    result = task_func(url, save_path, extract_path)

    assert result == extract_path

def test_task_func_with_invalid_url():
    url = "https://example.com/invalid_file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"

    result = task_func(url, save_path, extract_path)

    assert isinstance(result, str)
    assert "URL Error" in result

def test_task_func_with_existing_save_path():
    url = "https://example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"

    # Create a file at the save_path to simulate an existing file
    with open(save_path, "w") as f:
        f.write("Test content")

    result = task_func(url, save_path, extract_path)

    assert result == extract_path

    # Clean up the created file
    os.remove(save_path)

def test_task_func_with_existing_extract_path():
    url = "https://example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"

    # Create a directory at the extract_path to simulate an existing directory
    os.makedirs(extract_path)

    result = task_func(url, save_path, extract_path)

    assert result == extract_path

    # Clean up the created directory
    os.rmdir(extract_path)