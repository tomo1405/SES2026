import pytest
from src_1121 import task_func
import requests
import json

# Mocking the requests.get function to simulate API responses
class MockResponse:
    def __init__(self, text):
        self.text = text

def mock_requests_get(*args, **kwargs):
    if 'example.com' in args[0]:
        return MockResponse(json.dumps({"status": "success", "country": "USA"}))
    elif 'test.com' in args[0]:
        return MockResponse(json.dumps({"status": "fail", "message": "Private IP address"}))
    else:
        return MockResponse(json.dumps({"status": "fail", "message": "Invalid domain"}))

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_with_valid_urls():
    input_string = "Check out https://example.com and http://test.com"
    api_key = "fake_api_key"
    expected_output = {
        'example.com': {"status": "success", "country": "USA"},
        'test.com': {"status": "fail", "message": "Private IP address"}
    }
    assert task_func(input_string, api_key) == expected_output

def test_task_func_with_no_urls():
    input_string = "No URLs here"
    api_key = "fake_api_key"
    expected_output = {}
    assert task_func(input_string, api_key) == expected_output

def test_task_func_with_invalid_domain():
    input_string = "Invalid URL http://invalid-domain"
    api_key = "fake_api_key"
    expected_output = {
        'invalid-domain': {"status": "fail", "message": "Invalid domain"}
    }
    assert task_func(input_string, api_key) == expected_output