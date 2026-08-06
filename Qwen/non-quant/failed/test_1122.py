import pytest
from src_1122 import task_func
import requests
import json

# Mocking the requests.get function to avoid actual HTTP calls
class MockResponse:
    def __init__(self, text):
        self.text = text

def mock_requests_get(url):
    # Example JSON response for testing purposes
    example_json = '{"status":"success","country":"United States","regionName":"California","city":"San Francisco"}'
    return MockResponse(example_json)

@pytest.fixture
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func(mock_requests):
    myString = "Check out these websites: https://example.com and http://test.org"
    API_KEY = "dummy_api_key"
    
    expected_output = {
        "example.com": json.loads('{"status":"success","country":"United States","regionName":"California","city":"San Francisco"}'),
        "test.org": json.loads('{"status":"success","country":"United States","regionName":"California","city":"San Francisco"}')
    }
    
    result = task_func(myString, API_KEY)
    assert result == expected_output

def test_task_func_no_urls():
    myString = "No URLs here"
    API_KEY = "dummy_api_key"
    
    expected_output = {}
    
    result = task_func(myString, API_KEY)
    assert result == expected_output

def test_task_func_invalid_url():
    myString = "Invalid URL: https://example..com"
    API_KEY = "dummy_api_key"
    
    expected_output = {}
    
    result = task_func(myString, API_KEY)
    assert result == expected_output