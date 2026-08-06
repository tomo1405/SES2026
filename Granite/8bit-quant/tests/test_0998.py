import os
import pytest
import urllib.request
import zipfile
from src_0998 import task_func

TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"

def setup_module(module):
    os.makedirs(TARGET_DIR, exist_ok=True)

def teardown_module(module):
    if os.path.exists(TARGET_DIR):
        os.rmdir(TARGET_DIR)
    if os.path.exists(TARGET_ZIP_FILE):
        os.remove(TARGET_ZIP_FILE)

def test_task_func_valid_url():
    url = "https://example.com/myfile.zip"
    result = task_func(url)
    assert result == TARGET_DIR
    assert os.path.exists(os.path.join(TARGET_DIR, "myfile"))

def test_task_func_invalid_url():
    url = "https://example.com/invalidfile.zip"
    with pytest.raises(urllib.error.URLError):
        task_func(url)
    assert not os.path.exists(TARGET_DIR)

def test_task_func_invalid_zip_file():
    url = "https://example.com/invalidfile.zip"
    with pytest.raises(zipfile.BadZipFile):
        task_func(url)
    assert not os.path.exists(TARGET_DIR)