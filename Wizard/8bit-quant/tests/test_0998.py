python
import urllib.request
import os
import zipfile
import pytest

# Constants
TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"

def task_func(url):

    os.makedirs(TARGET_DIR, exist_ok=True)

    # context = ssl._create_unverified_context()
    # urllib.request.urlretrieve(url, TARGET_ZIP_FILE, context=context)
    urllib.request.urlretrieve(url, TARGET_ZIP_FILE)

    with zipfile.ZipFile(TARGET_ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(TARGET_DIR)

    if os.path.exists(TARGET_ZIP_FILE):
        os.remove(TARGET_ZIP_FILE)

    return TARGET_DIR

def test_task_func():
    # Test case 1: Download a zip file and extract it
    url = "https://www.example.com/example.zip"
    assert task_func(url) == "downloaded_files"

    # Test case 2: Download a non-zip file and extract it
    url = "https://www.example.com/example.txt"
    with pytest.raises(zipfile.BadZipFile):
        task_func(url)

    # Test case 3: Download a non-existent file
    url = "https://www.example.com/nonexistent.zip"
    with pytest.raises(urllib.error.URLError):
        task_func(url)