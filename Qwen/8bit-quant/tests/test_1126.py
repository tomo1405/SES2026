import pytest
from src_1126 import task_func
import requests
import json

# Mocking the requests.post function to simulate API responses
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def mock_post(url, headers, data):
    # Simulate a successful response
    if url == 'https://api.example.com/urls' and headers['Authorization'].startswith('Bearer '):
        return MockResponse({"message": "URL processed successfully"}, 200)
    else:
        raise Exception("Unexpected request")

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'post', mock_post)

def test_task_func_success():
    myString = "Check out this link: https://example.com"
    token = "valid_token"
    result = task_func(myString, token)
    assert result == {"message": "URL processed successfully"}

def test_task_func_invalid_url():
    myString = "No URL here"
    token = "valid_token"
    with pytest.raises(Exception) as excinfo:
        task_func(myString, token)
    assert str(excinfo.value) == "No URL found in the input string"

def test_task_func_invalid_token():
    myString = "Check out this link: https://example.com"
    token = "invalid_token"
    with pytest.raises(Exception) as excinfo:
        task_func(myString, token)
    assert str(excinfo.value) == "Unexpected request"