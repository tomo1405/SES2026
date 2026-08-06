import os
import pytest
import urllib.request
import zipfile
from src_0998 import task_func

TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"

def test_task_func_valid_url():
    url = "https://example.com/some_file.zip"
    result = task_func(url)
    assert result == TARGET_DIR
    assert os.path.exists(TARGET_DIR)
    assert os.path.exists(os.path.join(TARGET_DIR, "some_file.zip"))
    assert os.path.exists(TARGET_ZIP_FILE)

def test_task_func_invalid_url():
    url = "https://example.com/some_file.zip"
    with pytest.raises(urllib.error.URLError):
        task_func(url)
    assert not os.path.exists(TARGET_DIR)
    assert not os.path.exists(TARGET_ZIP_FILE)

def test_task_func_invalid_zip_file():
    url = "https://example.com/some_file.txt"
    with pytest.raises(zipfile.BadZipFile):
        task_func(url)
    assert not os.path.exists(TARGET_DIR)
    assert not os.path.exists(TARGET_ZIP_FILE)