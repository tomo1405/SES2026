import io
import json

import pytest
import requests
from src_1138 import task_func


# Mocking requests and bs4 for URL handling
class MockResponse:
    def __init__(self, text):
        self.text = text

def mock_requests_get(url, headers):
    if url == "http://example.com":
        return MockResponse("<html><body>Phone: +123 456-7890</body></html>")
    else:
        raise Exception("Unexpected URL")

# Mocking file handling for local files
def mock_open(filename, mode):
    if filename == "local_file.html":
        return io.StringIO("<html><body>Phone: +987 654-3210</body></html>")
    else:
        raise FileNotFoundError(f"File {filename} not found")

@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

@pytest.fixture(autouse=True)
def patch_open(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)

def test_task_func_with_url(tmpdir):
    url = "http://example.com"
    output_path = str(tmpdir / "output.json")
    expected_output = ['+123 456-7890']
    
    result = task_func(url, output_path)
    
    assert result == expected_output
    with open(output_path, 'r') as f:
        assert json.load(f) == expected_output

def test_task_func_with_local_file(tmpdir):
    url = "file://local_file.html"
    output_path = str(tmpdir / "output.json")
    expected_output = ['+987 654-3210']
    
    result = task_func(url, output_path)
    
    assert result == expected_output
    with open(output_path, 'r') as f:
        assert json.load(f) == expected_output

def test_task_func_invalid_url(tmpdir):
    url = "http://nonexistent.com"
    output_path = str(tmpdir / "output.json")
    
    with pytest.raises(Exception) as excinfo:
        task_func(url, output_path)
    
    assert str(excinfo.value) == "Unexpected URL"

def test_task_func_invalid_file(tmpdir):
    url = "file://nonexistent_file.html"
    output_path = str(tmpdir / "output.json")
    
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(url, output_path)
    
    assert str(excinfo.value) == "File nonexistent_file.html not found"