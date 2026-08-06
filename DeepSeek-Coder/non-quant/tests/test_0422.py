import pytest
from src_0422 import task_func
import requests
import os
import json
import time

# Mocking the requests.post function for testing purposes
class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def json(self):
        return {"status": "success"}

@pytest.fixture
def mock_requests_post(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse(200)
    monkeypatch.setattr(requests, "post", mock_post)

@pytest.fixture
def mock_directory(tmp_path):
    # Create a temporary directory with some files for testing
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    for i in range(3):
        with open(test_dir / f"file_{i}.txt", "w") as f:
            f.write("test")
    return str(test_dir)

def test_task_func(mock_requests_post, mock_directory):
    url = "http://test.com"
    metadata = {"key": "value"}
    result = task_func(url, mock_directory, metadata=metadata)
    assert len(result) == 3
    assert all(isinstance(code, int) for code in result)