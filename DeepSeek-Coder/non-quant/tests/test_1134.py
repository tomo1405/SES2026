import pytest
from src_1134 import task_func
import requests
import json

@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.HTTPError("Mocked HTTP Error")

    return MockResponse({"key": "value"}, 200)

@pytest.fixture
def mock_requests_get(monkeypatch):
    def mock_get(*args, **kwargs):
        response = mock_response()
        return response

    monkeypatch.setattr(requests, 'get', mock_get)

def test_task_func(mock_requests_get, monkeypatch):
    filename = task_func("http://example.com", "endpoint", "prefix_")
    assert "prefix_endpoint.json" == filename
    with open(filename, 'r') as f:
        data = json.load(f)
    assert data == {"key": "value"}