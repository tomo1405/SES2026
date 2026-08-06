import pytest
from src_1013 import task_func
from unittest.mock import patch, Mock
from pathlib import Path
import zipfile

# Constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

def test_task_func_success(mocker):
    url = "http://example.com/file.zip"
    filename = "file.zip"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.iter_content.return_value = [b"data"]
    
    mocker.patch('requests.get', return_value=mock_response)
    
    result, files = task_func(url, filename)
    
    assert result == "Download and extraction successful"
    assert files == ["data"]

def test_task_func_download_failure(mocker):
    url = "http://example.com/file.zip"
    filename = "file.zip"
    mock_response = Mock()
    mock_response.status_code = 404
    
    mocker.patch('requests.get', return_value=mock_response)
    
    result, files = task_func(url, filename)
    
    assert result == "Download failed: HTTP status code 404"
    assert files == []

def test_task_func_request_exception(mocker):
    url = "http://example.com/file.zip"
    filename = "file.zip"
    mocker.patch('requests.get', side_effect=requests.exceptions.RequestException("Connection error"))
    
    result, files = task_func(url, filename)
    
    assert result == "Error: Connection error"
    assert files == []

def test_task_func_invalid_zip_file(mocker):
    url = "http://example.com/file.zip"
    filename = "file.zip"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.iter_content.return_value = [b"data"]
    
    mocker.patch('requests.get', return_value=mock_response)
    mocker.patch('zipfile.ZipFile', side_effect=zipfile.BadZipFile("Invalid zip file"))
    
    result, files = task_func(url, filename)
    
    assert result == "Error: Invalid zip file: Invalid zip file"
    assert files == []