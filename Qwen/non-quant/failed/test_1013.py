import pytest
from src_1013 import task_func
from unittest.mock import patch, MagicMock
from pathlib import Path
import zipfile

# Mocking constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

@pytest.fixture
def mock_requests_get(monkeypatch):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.iter_content.return_value = [b'data']
    monkeypatch.setattr('requests.get', lambda url, stream, timeout: mock_response)
    return mock_response

@pytest.fixture
def mock_zipfile(monkeypatch):
    class MockZipFile:
        def __init__(self, *args, **kwargs):
            pass

        def extractall(self, path):
            (path / "file1.txt").touch()
            (path / "file2.txt").touch()

    monkeypatch.setattr('zipfile.ZipFile', MockZipFile)
    return MockZipFile

def test_task_func_success(mock_requests_get, mock_zipfile):
    url = "http://example.com/file.zip"
    filename = "file.zip"
    result, files = task_func(url, filename)
    assert result == "Download and extraction successful"
    assert files == ["file1.txt", "file2.txt"]
    assert (DOWNLOAD_DIR / filename).exists()
    assert (ZIP_DIR / "file").exists()
    assert (ZIP_DIR / "file" / "file1.txt").exists()
    assert (ZIP_DIR / "file" / "file2.txt").exists()

def test_task_func_download_failure(mock_requests_get):
    mock_requests_get.status_code = 404
    url = "http://example.com/file.zip"
    filename = "file.zip"
    result, files = task_func(url, filename)
    assert result == "Download failed: HTTP status code 404"
    assert files == []

def test_task_func_request_exception():
    url = "http://example.com/file.zip"
    filename = "file.zip"
    with patch('requests.get', side_effect=requests.exceptions.RequestException("Connection error")):
        result, files = task_func(url, filename)
    assert result == "Error: Connection error"
    assert files == []

def test_task_func_invalid_zip_file(mock_requests_get):
    url = "http://example.com/file.zip"
    filename = "file.zip"
    with patch('zipfile.ZipFile', side_effect=zipfile.BadZipFile("Invalid zip file")):
        result, files = task_func(url, filename)
    assert result == "Error: Invalid zip file: Invalid zip file"
    assert files == []