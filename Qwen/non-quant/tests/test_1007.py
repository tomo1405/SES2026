from unittest.mock import MagicMock, patch

import requests
from src_1007 import task_func


@patch('src_1007.os')
@patch('src_1007.requests.get')
def test_task_func_valid_zip(mock_requests_get, mock_os):
    # Mocking the response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {'Content-Type': 'application/zip'}
    mock_response.content = b'zip_content'
    mock_requests_get.return_value = mock_response

    # Mocking os.path.exists and os.makedirs
    mock_os.path.exists.side_effect = [False, True]
    mock_os.makedirs.return_value = None

    url = "http://example.com/file.zip"
    download_path = "/tmp/downloads/"
    expected_extract_path = "/tmp/downloads/file"

    result = task_func(url, download_path)

    assert result == expected_extract_path
    mock_requests_get.assert_called_once_with(url, timeout=5)
    mock_os.makedirs.assert_called_once_with(download_path)
    mock_os.makedirs.assert_called_with(expected_extract_path)

@patch('src_1007.os')
@patch('src_1007.requests.get')
def test_task_func_invalid_content_type(mock_requests_get, mock_os):
    # Mocking the response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {'Content-Type': 'text/plain'}
    mock_requests_get.return_value = mock_response

    url = "http://example.com/file.txt"
    download_path = "/tmp/downloads/"

    result = task_func(url, download_path)

    assert result == "Error: The URL does not point to a ZIP file."
    mock_requests_get.assert_called_once_with(url, timeout=5)
    mock_os.makedirs.assert_not_called()

@patch('src_1007.os')
@patch('src_1007.requests.get')
def test_task_func_download_failure(mock_requests_get, mock_os):
    # Mocking the response object to raise an exception
    mock_requests_get.side_effect = requests.RequestException("Connection error")

    url = "http://example.com/file.zip"
    download_path = "/tmp/downloads/"

    result = task_func(url, download_path)

    assert result == "Error: Unable to download the file from the provided URL."
    mock_requests_get.assert_called_once_with(url, timeout=5)
    mock_os.makedirs.assert_not_called()

@patch('src_1007.os')
@patch('src_1007.requests.get')
def test_task_func_bad_zip_file(mock_requests_get, mock_os):
    # Mocking the response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {'Content-Type': 'application/zip'}
    mock_response.content = b'invalid_zip_content'
    mock_requests_get.return_value = mock_response

    # Mocking os.path.exists and os.makedirs
    mock_os.path.exists.side_effect = [False, True]
    mock_os.makedirs.return_value = None

    url = "http://example.com/file.zip"
    download_path = "/tmp/downloads/"

    result = task_func(url, download_path)

    assert result == "Error: The downloaded file is not a valid ZIP file."
    mock_requests_get.assert_called_once_with(url, timeout=5)
    mock_os.makedirs.assert_called_once_with(download_path)