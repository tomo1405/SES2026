import pytest
from src_0998 import task_func
import os
import zipfile

# Mocking urllib.request.urlretrieve and zipfile.ZipFile to avoid actual file operations
from unittest.mock import patch, MagicMock

@patch('src_0998.urllib.request.urlretrieve')
@patch('src_0998.zipfile.ZipFile')
def test_task_func(mock_zipfile, mock_urlretrieve):
    # Mock the URL and expected behavior
    url = "http://example.com/sample.zip"
    mock_urlretrieve.return_value = None  # Simulate successful download

    # Mock the zipfile extraction
    mock_zip_ref = MagicMock()
    mock_zip_ref.extractall.return_value = None
    mock_zipfile.return_value.__enter__.return_value = mock_zip_ref

    # Call the function
    result = task_func(url)

    # Assertions
    assert result == "downloaded_files"
    mock_urlretrieve.assert_called_once_with(url, "downloaded_files.zip")
    mock_zipfile.assert_called_once_with("downloaded_files.zip", "r")
    mock_zip_ref.extractall.assert_called_once_with("downloaded_files")

    # Check if the directory exists
    assert os.path.exists("downloaded_files")

    # Clean up the directory after test
    os.rmdir("downloaded_files")

@patch('src_0998.os.remove')
@patch('src_0998.os.path.exists')
def test_task_func_file_cleanup(mock_path_exists, mock_remove):
    # Mock the existence of the zip file
    mock_path_exists.return_value = True

    # Call the function
    task_func("http://example.com/sample.zip")

    # Assertion
    mock_remove.assert_called_once_with("downloaded_files.zip")

@patch('src_0998.urllib.request.urlretrieve', side_effect=Exception("Network error"))
def test_task_func_exception_handling(mock_urlretrieve):
    # Call the function and expect an exception
    with pytest.raises(Exception) as excinfo:
        task_func("http://example.com/sample.zip")

    # Assertion
    assert str(excinfo.value) == "Network error"