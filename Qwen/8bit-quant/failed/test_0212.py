import pytest
from src_0212 import task_func
import os
import zipfile
import tempfile
import requests_mock

def test_task_func_with_valid_url_and_headers():
    # Arrange
    url = "http://example.com/test.zip"
    headers = {'accept': 'application/octet-stream'}
    expected_files = ['file1.txt', 'file2.txt']
    
    with tempfile.TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as m:
            m.get(url, content=b"zip_content")
            
            # Act
            result = task_func(url, temp_dir, headers=headers)
            
            # Assert
            assert sorted(result) == sorted(expected_files)

def test_task_func_with_default_headers():
    # Arrange
    url = "http://example.com/test.zip"
    expected_files = ['file1.txt', 'file2.txt']
    
    with tempfile.TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as m:
            m.get(url, content=b"zip_content")
            
            # Act
            result = task_func(url, temp_dir)
            
            # Assert
            assert sorted(result) == sorted(expected_files)

def test_task_func_with_nonexistent_url():
    # Arrange
    url = "http://example.com/nonexistent.zip"
    expected_error_message = "404 Client Error: Not Found for url: http://example.com/nonexistent.zip"
    
    with tempfile.TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as m:
            m.get(url, status_code=404)
            
            # Act & Assert
            with pytest.raises(requests.exceptions.HTTPError) as excinfo:
                task_func(url, temp_dir)
            assert str(excinfo.value) == expected_error_message

def test_task_func_with_invalid_zip_content():
    # Arrange
    url = "http://example.com/invalid.zip"
    expected_error_message = "Invalid ZIP file"
    
    with tempfile.TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as m:
            m.get(url, content=b"invalid_content")
            
            # Act & Assert
            with pytest.raises(zipfile.BadZipFile) as excinfo:
                task_func(url, temp_dir)
            assert str(excinfo.value) == expected_error_message