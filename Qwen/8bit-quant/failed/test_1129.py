import pytest
from src_1129 import task_func
import os
import json
import hashlib
import base64
import time

# Mocking functions and objects
class MockOpen:
    def __init__(self, content):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def read(self):
        return self.content

def mock_json_load(mock_file):
    return json.loads(mock_file.read())

def mock_os_getcwd():
    return "/mock/path"

def mock_time_time():
    return 1633072800  # Fixed timestamp for predictable file name

def mock_hashlib_sha256(data):
    class MockHash:
        def digest(self):
            return b'mocked_hash'
    return MockHash()

def mock_base64_b64encode(data):
    return b'mocked_encoded'

def mock_open(file_path, mode):
    if file_path == "/mock/path/A_hashed_1633072800.txt":
        return MockOpen("")
    else:
        raise FileNotFoundError("File not found")

# Patching
@pytest.fixture(autouse=True)
def patch_dependencies(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)
    monkeypatch.setattr('json.load', mock_json_load)
    monkeypatch.setattr('os.getcwd', mock_os_getcwd)
    monkeypatch.setattr('time.time', mock_time_time)
    monkeypatch.setattr('hashlib.sha256', mock_hashlib_sha256)
    monkeypatch.setattr('base64.b64encode', mock_base64_b64encode)

def test_task_func():
    # Prepare mock JSON content
    mock_json_content = '{"A": {"key1": {"maindata": [{"Info": "test_info"}]}}}'
    
    # Call the function
    result = task_func("/path/to/file.json", "key1")
    
    # Expected result
    expected_result = "/mock/path/key1_hashed_1633072800.txt"
    
    # Assertions
    assert result == expected_result
    
    # Verify file content
    with open(expected_result, 'r') as f:
        content = f.read()
        assert content == "bW9ja2VkX2VuY29kZWQ="  # Base64 encoded "mocked_encoded"