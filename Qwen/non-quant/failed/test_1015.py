import pytest
from src_1015 import task_func
import requests
import pandas as pd

# Mocking the requests module
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError(f"HTTP error occurred: {self.status_code}")

def test_task_func_valid_url(mocker):
    # Mock the requests.get call to return a successful response
    mock_json_data = [{"key": "value"}]
    mock_response = MockResponse(mock_json_data, 200)
    mocker.patch('requests.get', return_value=mock_response)

    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.equals(pd.DataFrame(mock_json_data))
    assert plot is not None

def test_task_func_invalid_url(mocker):
    # Mock the requests.get call to return a non-200 status code
    mock_response = MockResponse({}, 404)
    mocker.patch('requests.get', return_value=mock_response)

    api_url = "https://api.example.com/data"
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        task_func(api_url)

    assert str(excinfo.value) == "HTTP error occurred: 404"

def test_task_func_empty_response(mocker):
    # Mock the requests.get call to return an empty JSON response
    mock_json_data = []
    mock_response = MockResponse(mock_json_data, 200)
    mocker.patch('requests.get', return_value=mock_response)

    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)

    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert plot is None

def test_task_func_non_string_url():
    api_url = 12345  # Non-string input
    with pytest.raises(TypeError) as excinfo:
        task_func(api_url)

    assert str(excinfo.value) == "api_url must be a string"