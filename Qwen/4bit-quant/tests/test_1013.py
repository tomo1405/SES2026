import zipfile

import pytest
import requests
from src_1013 import task_func


# Mocking the requests module
class MockResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    def iter_content(self, chunk_size=1024):
        return [self.content]

def mock_requests_get(url, stream, timeout):
    if url == "http://example.com/test.zip":
        return MockResponse(200, b"zipfilecontent")
    else:
        return MockResponse(404, b"")

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_success(tmp_path):
    # Set up temporary directories
    download_dir = tmp_path / "downloads"
    zip_dir = tmp_path / "unzipped_files"
    download_dir.mkdir(parents=True, exist_ok=True)
    zip_dir.mkdir(parents=True, exist_ok=True)

    # Mock the zipfile module to avoid actual extraction
    class MockZipFile:
        def __init__(self, file, mode):
            pass

        def extractall(self, path):
            (path / "file1.txt").touch()
            (path / "file2.txt").touch()

    monkeypatch.setattr(zipfile, 'ZipFile', MockZipFile)

    result, files = task_func("http://example.com/test.zip", "test.zip")
    assert result == "Download and extraction successful"
    assert files == ["file1.txt", "file2.txt"]

def test_task_func_download_failure(tmp_path):
    result, files = task_func("http://example.com/nonexistent.zip", "nonexistent.zip")
    assert result == "Download failed: HTTP status code 404"
    assert files == []

def test_task_func_request_exception(tmp_path, monkeypatch):
    def raise_exception(*args, **kwargs):
        raise requests.exceptions.RequestException("Connection error")

    monkeypatch.setattr(requests, 'get', raise_exception)

    result, files = task_func("http://example.com/test.zip", "test.zip")
    assert result == "Error: Connection error"
    assert files == []

def test_task_func_bad_zip_file(tmp_path, monkeypatch):
    def mock_requests_get_with_bad_zip(url, stream, timeout):
        if url == "http://example.com/badzip.zip":
            return MockResponse(200, b"badzipcontent")
        else:
            return MockResponse(404, b"")

    monkeypatch.setattr(requests, 'get', mock_requests_get_with_bad_zip)

    result, files = task_func("http://example.com/badzip.zip", "badzip.zip")
    assert result.startswith("Error: Invalid zip file:")
    assert files == []