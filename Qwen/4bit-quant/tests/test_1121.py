import pytest
from src_1121 import task_func
import requests
import json

# Mocking the requests.get function to simulate API responses
class MockResponse:
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data

def mock_requests_get(url):
    # Simulate different responses based on the URL
    if "example.com" in url:
        return MockResponse({"status": "success", "country": "US"})
    elif "test.com" in url:
        return MockResponse({"status": "fail", "message": "Invalid API key"})
    else:
        return MockResponse({"status": "error", "message": "Not found"})

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_with_valid_url():
    myString = "Check out https://example.com and http://test.com"
    API_KEY = "valid_api_key"
    expected_output = {
        "example.com": {"status": "success", "country": "US"},
        "test.com": {"status": "fail", "message": "Invalid API key"}
    }
    assert task_func(myString, API_KEY) == expected_output

def test_task_func_with_no_urls():
    myString = "No URLs here"
    API_KEY = "valid_api_key"
    expected_output = {}
    assert task_func(myString, API_KEY) == expected_output

def test_task_func_with_invalid_api_key():
    myString = "Check out https://example.com"
    API_KEY = "invalid_api_key"
    expected_output = {
        "example.com": {"status": "error", "message": "Not found"}
    }
    assert task_func(myString, API_KEY) == expected_output