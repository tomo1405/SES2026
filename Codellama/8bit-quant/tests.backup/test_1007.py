import pytest
from src_1007 import task_func

def test_task_func_valid_url():
    url = "https://www.example.com/file.zip"
    download_path = "mnt/data/downloads/"
    expected_extract_path = os.path.splitext(os.path.join(download_path, os.path.basename(url)))[0]
    assert task_func(url, download_path) == expected_extract_path

def test_task_func_invalid_url():
    url = "https://www.example.com/file.txt"
    download_path = "mnt/data/downloads/"
    assert task_func(url, download_path) == "Error: The URL does not point to a ZIP file."

def test_task_func_download_error():
    url = "https://www.example.com/file.zip"
    download_path = "mnt/data/downloads/"
    with pytest.raises(requests.RequestException):
        task_func(url, download_path)

def test_task_func_bad_zip_file():
    url = "https://www.example.com/file.zip"
    download_path = "mnt/data/downloads/"
    with pytest.raises(BadZipFile):
        task_func(url, download_path)

def test_task_func_runtime_error():
    url = "https://www.example.com/file.zip"
    download_path = "mnt/data/downloads/"
    with pytest.raises(RuntimeError):
        task_func(url, download_path)