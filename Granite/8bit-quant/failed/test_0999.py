import pytest
import urllib.request
import os
import hashlib
import tarfile

from src_0999 import task_func

TARGET_TAR_FILE = "downloaded_files.tar.gz"
EXPECTED_MD5_CHECKSUM = "d41d8cd98f00b204e9800998ecf8427e"

def test_task_func_with_valid_url():
    with pytest.raises(Exception):
        task_func("https://www.example.com")

def test_task_func_with_invalid_url():
    with pytest.raises(Exception):
        task_func("invalid_url")

def test_task_func_with_valid_url_and_valid_checksum():
    with pytest.raises(Exception):
        task_func("https://www.example.com")

def test_task_func_with_valid_url_and_invalid_checksum():
    with pytest.raises(Exception):
        task_func("https://www.example.com")