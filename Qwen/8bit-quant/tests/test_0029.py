import pytest
import requests
from src_0029 import task_func


# Mocking the requests.post function
class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

def mock_post(url, json_data):
    # Example response data
    return MockResponse(200, {"status": "success", "data": json_data})

@pytest.fixture
def mock_requests_post(monkeypatch):
    monkeypatch.setattr(requests, 'post', mock_post)

def test_task_func_success(mock_requests_post):
    data = {"key": "value"}
    url = "http://your-api-url.com"
    response = task_func(data, url)
    
    assert response.status_code == 200
    assert response.json() == {"status": "success", "data": {"payload": "eyJrZXkiOiAidmFsdWUifQ=="}}  # Base64 encoded JSON of {"key": "value"}

def test_task_func_failure(mock_requests_post):
    data = {"key": "value"}
    url = "http://your-api-url.com"
    # Modify the mock to simulate a failure
    def mock_post_failure(url, json_data):
        return MockResponse(500, {"status": "error"})
    
    monkeypatch.setattr(requests, 'post', mock_post_failure)
    
    response = task_func(data, url)
    
    assert response.status_code == 500
    assert response.json() == {"status": "error"}