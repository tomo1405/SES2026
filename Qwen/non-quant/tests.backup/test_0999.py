import pytest
from unittest.mock import patch, MagicMock
from src_0999 import task_func
import os
import hashlib
import tarfile

# Constants
TARGET_TAR_FILE = "downloaded_files.tar.gz"
EXPECTED_MD5_CHECKSUM = "d41d8cd98f00b204e9800998ecf8427e"

def test_task_func_url_retrieval_failure():
    url = "http://example.com/failure"
    with patch('urllib.request.urlretrieve', side_effect=Exception("Network error")):
        assert not task_func(url)
        assert not os.path.exists(TARGET_TAR_FILE)

def test_task_func_md5_mismatch():
    url = "http://example.com/mismatch"
    with patch('urllib.request.urlretrieve') as mock_retrieve:
        mock_retrieve.return_value = None
        with open(TARGET_TAR_FILE, 'wb') as f:
            f.write(b'test data')
        assert not task_func(url)
        assert not os.path.exists(TARGET_TAR_FILE)

def test_task_func_md5_match_and_extraction():
    url = "http://example.com/success"
    expected_content = b'test data'
    expected_md5 = hashlib.md5(expected_content).hexdigest()
    assert expected_md5 != EXPECTED_MD5_CHECKSUM  # Ensure this is different for the test

    with patch('urllib.request.urlretrieve') as mock_retrieve:
        mock_retrieve.return_value = None
        with open(TARGET_TAR_FILE, 'wb') as f:
            f.write(expected_content)
        assert not task_func(url)
        assert not os.path.exists(TARGET_TAR_FILE)

    # Now test with correct checksum
    with patch('urllib.request.urlretrieve') as mock_retrieve:
        mock_retrieve.return_value = None
        with open(TARGET_TAR_FILE, 'wb') as f:
            f.write(expected_content)
        with patch('hashlib.md5().hexdigest', return_value=EXPECTED_MD5_CHECKSUM):
            with patch('tarfile.open') as mock_tar_open:
                mock_tar_open.return_value.__enter__.return_value = MagicMock()
                assert task_func(url)
                mock_tar_open.assert_called_once_with(TARGET_TAR_FILE, "r:gz")
                mock_tar_open.return_value.extractall.assert_called_once()
                assert not os.path.exists(TARGET_TAR_FILE)

def test_task_func_file_cleanup_on_failure():
    url = "http://example.com/cleanup"
    with patch('urllib.request.urlretrieve', side_effect=Exception("Network error")):
        task_func(url)
        assert not os.path.exists(TARGET_TAR_FILE)

    with patch('urllib.request.urlretrieve') as mock_retrieve:
        mock_retrieve.return_value = None
        with open(TARGET_TAR_FILE, 'wb') as f:
            f.write(b'test data')
        with patch('hashlib.md5().hexdigest', return_value="wrong_checksum"):
            task_func(url)
            assert not os.path.exists(TARGET_TAR_FILE)