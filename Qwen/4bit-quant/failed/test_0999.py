import pytest
from src_0999 import task_func
import os
import hashlib
import tarfile

# Constants
TARGET_TAR_FILE = "downloaded_files.tar.gz"
EXPECTED_MD5_CHECKSUM = "d41d8cd98f00b204e9800998ecf8427e"

def test_task_func_success(mocker):
    # Mock the urlretrieve to simulate a successful download
    mock_urlretrieve = mocker.patch('urllib.request.urlretrieve')
    
    # Mock the file content to match the expected MD5 checksum
    mock_file_content = b""
    mock_md5 = hashlib.md5(mock_file_content).hexdigest()
    assert mock_md5 == EXPECTED_MD5_CHECKSUM

    # Create a temporary tar.gz file with the mock content
    with tarfile.open(TARGET_TAR_FILE, "w:gz") as tar:
        pass  # No files added to the tarball for this test

    # Call the function
    result = task_func("http://example.com/download")

    # Check if the function returns True
    assert result is True

    # Check if the tar.gz file was removed
    assert not os.path.exists(TARGET_TAR_FILE)

def test_task_func_download_failure(mocker):
    # Mock the urlretrieve to simulate a download failure
    mock_urlretrieve = mocker.patch('urllib.request.urlretrieve', side_effect=Exception("Download failed"))

    # Call the function
    result = task_func("http://example.com/download")

    # Check if the function returns False
    assert result is False

def test_task_func_md5_mismatch(mocker):
    # Mock the urlretrieve to simulate a successful download
    mock_urlretrieve = mocker.patch('urllib.request.urlretrieve')
    
    # Mock the file content to have a different MD5 checksum
    mock_file_content = b"some data"
    mock_md5 = hashlib.md5(mock_file_content).hexdigest()
    assert mock_md5 != EXPECTED_MD5_CHECKSUM

    # Create a temporary tar.gz file with the mock content
    with tarfile.open(TARGET_TAR_FILE, "w:gz") as tar:
        tar.addfile(tarfile.TarInfo(name="test.txt"), fileobj=mocker.Mock(read=lambda: mock_file_content))

    # Call the function
    result = task_func("http://example.com/download")

    # Check if the function returns False
    assert result is False

    # Check if the tar.gz file was removed
    assert not os.path.exists(TARGET_TAR_FILE)