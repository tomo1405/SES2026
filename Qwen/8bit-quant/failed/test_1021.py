import pytest
from src_1021 import task_func
import requests
import json

# Mocking the requests.get function
class MockResponse:
    def __init__(self, content, status_code=200):
        self.content = content
        self.status_code = status_code

    def json(self):
        return json.loads(self.content.decode())

def mock_requests_get(*args, **kwargs):
    if args[0] == "http://api.example.com/data":
        return MockResponse(b'{"key": "value"}')
    else:
        raise Exception("Unexpected URL")

# Patching the requests.get function
@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_default_encoding():
    result = task_func()
    assert result == {"key": "value"}

def test_task_func_with_from_encoding():
    result = task_func(from_encoding="utf-8")
    assert result == {"key": "value"}

def test_task_func_with_to_encoding():
    result = task_func(to_encoding="ascii")
    assert result == {"key": "value"}

def test_task_func_with_empty_content():
    response = MockResponse(b'')
    with pytest.raises(ValueError) as excinfo:
        task_func(url="http://api.example.com/empty")
    assert str(excinfo.value) == "Unable to detect encoding for non-empty content"

def test_task_func_with_invalid_url():
    with pytest.raises(Exception) as excinfo:
        task_func(url="http://api.example.com/invalid")
    assert str(excinfo.value) == "Unexpected URL"