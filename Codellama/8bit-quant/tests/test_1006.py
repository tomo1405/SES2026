import urllib

import pytest
from src_1006 import task_func


def test_task_func_valid_url():
    url = "https://www.example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    expected_extract_path = "extracted_files"

    assert task_func(url, save_path, extract_path) == expected_extract_path

def test_task_func_invalid_url():
    url = "https://www.example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    expected_error = "URL Error: <error message>"

    with pytest.raises(urllib.error.URLError) as e:
        task_func(url, save_path, extract_path)

    assert str(e.value) == expected_error