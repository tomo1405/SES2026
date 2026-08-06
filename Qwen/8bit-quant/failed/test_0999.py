import pytest
from unittest.mock import patch, MagicMock
from src_0999 import task_func

@patch('src_0999.urllib.request.urlretrieve')
@patch('src_0999.hashlib.md5')
@patch('src_0999.tarfile.open')
@patch('src_0999.os.remove')
def test_task_func_success(mock_os_remove, mock_tarfile_open, mock_md5, mock_urlretrieve):
    # Mock the urlretrieve to succeed
    mock_urlretrieve.return_value = None

    # Mock the md5 hash to match the expected checksum
    mock_md5_instance = MagicMock()
    mock_md5_instance.hexdigest.return_value = "d41d8cd98f00b204e9800998ecf8427e"
    mock_md5.return_value = mock_md5_instance

    # Mock the tarfile extraction
    mock_tar_ref = MagicMock()
    mock_tarfile_open.return_value = mock_tar_ref

    # Call the function
    result = task_func("http://example.com/file.tar.gz")

    # Assertions
    assert result is True
    mock_urlretrieve.assert_called_once_with("http://example.com/file.tar.gz", "downloaded_files.tar.gz")
    mock_md5.assert_called_once()
    mock_tar_ref.extractall.assert_called_once()
    mock_os_remove.assert_called_with("downloaded_files.tar.gz")

@patch('src_0999.urllib.request.urlretrieve')
def test_task_func_urlretrieve_failure(mock_urlretrieve):
    # Mock the urlretrieve to fail
    mock_urlretrieve.side_effect = Exception("Failed to download")

    # Call the function
    result = task_func("http://example.com/file.tar.gz")

    # Assertions
    assert result is False
    mock_urlretrieve.assert_called_once_with("http://example.com/file.tar.gz", "downloaded_files.tar.gz")

@patch('src_0999.urllib.request.urlretrieve')
@patch('src_0999.hashlib.md5')
def test_task_func_md5_mismatch(mock_md5, mock_urlretrieve):
    # Mock the urlretrieve to succeed
    mock_urlretrieve.return_value = None

    # Mock the md5 hash to mismatch the expected checksum
    mock_md5_instance = MagicMock()
    mock_md5_instance.hexdigest.return_value = "wrong_checksum"
    mock_md5.return_value = mock_md5_instance

    # Call the function
    result = task_func("http://example.com/file.tar.gz")

    # Assertions
    assert result is False
    mock_urlretrieve.assert_called_once_with("http://example.com/file.tar.gz", "downloaded_files.tar.gz")
    mock_md5.assert_called_once()

@patch('src_0999.urllib.request.urlretrieve')
@patch('src_0999.hashlib.md5')
@patch('src_0999.tarfile.open')
@patch('src_0999.os.remove')
def test_task_func_tarfile_extraction_failure(mock_os_remove, mock_tarfile_open, mock_md5, mock_urlretrieve):
    # Mock the urlretrieve to succeed
    mock_urlretrieve.return_value = None

    # Mock the md5 hash to match the expected checksum
    mock_md5_instance = MagicMock()
    mock_md5_instance.hexdigest.return_value = "d41d8cd98f00b204e9800998ecf8427e"
    mock_md5.return_value = mock_md5_instance

    # Mock the tarfile extraction to fail
    mock_tar_ref = MagicMock()
    mock_tar_ref.extractall.side_effect = Exception("Failed to extract")
    mock_tarfile_open.return_value = mock_tar_ref

    # Call the function
    result = task_func("http://example.com/file.tar.gz")

    # Assertions
    assert result is False
    mock_urlretrieve.assert_called_once_with("http://example.com/file.tar.gz", "downloaded_files.tar.gz")
    mock_md5.assert_called_once()
    mock_tar_ref.extractall.assert_called_once()
    mock_os_remove.assert_called_with("downloaded_files.tar.gz")