import pytest
from src_1006 import task_func
import os
import zipfile

# Mocking urllib.request.urlretrieve and zipfile.ZipFile for testing purposes
from unittest.mock import patch, MagicMock

@patch('src_1006.urllib.request.urlretrieve')
@patch('src_1006.zipfile.ZipFile')
def test_task_func_success(mock_zipfile, mock_urlretrieve):
    # Arrange
    url = "http://example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    mock_urlretrieve.return_value = None
    mock_zipfile.return_value.extractall.return_value = None

    # Act
    result = task_func(url, save_path, extract_path)

    # Assert
    assert result == extract_path
    mock_urlretrieve.assert_called_once_with(url, save_path)
    mock_zipfile.assert_called_once_with(save_path, 'r')
    mock_zipfile.return_value.extractall.assert_called_once_with(extract_path)
    assert not os.path.exists(save_path)

@patch('src_1006.urllib.request.urlretrieve', side_effect=urllib.error.URLError("Test URLError"))
def test_task_func_url_error(mock_urlretrieve):
    # Arrange
    url = "http://example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"

    # Act
    result = task_func(url, save_path, extract_path)

    # Assert
    assert result == "URL Error: Test URLError"
    mock_urlretrieve.assert_called_once_with(url, save_path)
    assert not os.path.exists(save_path)

def test_task_func_existing_save_path():
    # Arrange
    url = "http://example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    open(save_path, 'a').close()  # Create an empty file to simulate existing save_path

    # Act
    result = task_func(url, save_path, extract_path)

    # Assert
    assert result == extract_path
    assert not os.path.exists(save_path)

def test_task_func_existing_extract_path():
    # Arrange
    url = "http://example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    os.makedirs(extract_path)  # Create the directory to simulate existing extract_path

    # Act
    result = task_func(url, save_path, extract_path)

    # Assert
    assert result == extract_path
    assert not os.path.exists(save_path)