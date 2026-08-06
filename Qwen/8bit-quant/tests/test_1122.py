import pytest
from src_1122 import task_func
import requests
import json

# Mocking the requests.get function to simulate API responses
class MockResponse:
    def __init__(self, text):
        self.text = text

    def json(self):
        return json.loads(self.text)

def mock_requests_get(url):
    # Simulate different responses based on the URL
    if "example.com" in url:
        return MockResponse('{"status":"success","country":"United States"}')
    elif "test.com" in url:
        return MockResponse('{"status":"fail"}')
    else:
        return MockResponse('{"status":"unknown"}')

@pytest.fixture
def monkeypatch_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func(monkeypatch_requests):
    myString = "Check out https://example.com and http://test.com"
    API_KEY = "dummy_api_key"
    
    result = task_func(myString, API_KEY)
    
    assert isinstance(result, dict)
    assert "example.com" in result
    assert "test.com" in result
    assert result["example.com"]["status"] == "success"
    assert result["test.com"]["status"] == "fail"

def test_task_func_no_urls():
    myString = "No URLs here"
    API_KEY = "dummy_api_key"
    
    result = task_func(myString, API_KEY)
    
    assert isinstance(result, dict)
    assert len(result) == 0

def test_task_func_invalid_url():
    myString = "Invalid URL: https://invalid-url"
    API_KEY = "dummy_api_key"
    
    result = task_func(myString, API_KEY)
    
    assert isinstance(result, dict)
    assert "invalid-url" in result
    assert result["invalid-url"]["status"] == "unknown"