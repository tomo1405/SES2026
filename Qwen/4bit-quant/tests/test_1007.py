import os
from unittest.mock import mock_open, patch

from src_1007 import task_func


@patch('src_1007.requests.get')
@patch('src_1007.os.makedirs')
@patch('src_1007.ZipFile')
def test_task_func_success(mock_zipfile, mock_makedirs, mock_get):
    url = "http://example.com/file.zip"
    download_path = "/tmp/downloads/"
    file_name = os.path.join(download_path, "file.zip")
    extract_path = os.path.splitext(file_name)[0]

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "application/zip"}
    mock_response.content = b"zip_content"

    mock_zipfile.return_value.extractall.return_value = None

    result = task_func(url, download_path)

    assert result == extract_path
    mock_get.assert_called_once_with(url, timeout=5)
    mock_makedirs.assert_any_call(download_path)
    mock_makedirs.assert_any_call(extract_path)
    mock_open().write.assert_called_once_with(b"zip_content")

@patch('src_1007.requests.get')
def test_task_func_non_zip_content_type(mock_get):
    url = "http://example.com/file.txt"
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "text/plain"}

    result = task_func(url)

    assert result == "Error: The URL does not point to a ZIP file."

@patch('src_1007.requests.get')
def test_task_func_download_failure(mock_get):
    url = "http://example.com/file.zip"
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    result = task_func(url)

    assert result == "Error: Unable to download the file from the provided URL."

@patch('src_1007.requests.get')
@patch('src_1007.ZipFile')
def test_task_func_bad_zip_file(mock_zipfile, mock_get):
    url = "http://example.com/file.zip"
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "application/zip"}
    mock_response.content = b"zip_content"

    mock_zipfile.side_effect = BadZipFile

    result = task_func(url)

    assert result == "Error: The downloaded file is not a valid ZIP file."