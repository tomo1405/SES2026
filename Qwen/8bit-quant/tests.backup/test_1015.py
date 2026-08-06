import pytest
from src_1015 import task_func
import requests
import pandas as pd

# Mocking the requests.get function to simulate API responses
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError(f"HTTP error occurred: status code {self.status_code}")

def test_task_func_with_valid_api_url(mocker):
    # Mock a successful API response
    mock_json_data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    mock_response = MockResponse(mock_json_data, 200)
    mocker.patch('requests.get', return_value=mock_response)

    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.equals(pd.DataFrame(mock_json_data))
    assert plot is not None

def test_task_func_with_invalid_api_url(mocker):
    # Mock an unsuccessful API response
    mock_response = MockResponse({}, 404)
    mocker.patch('requests.get', return_value=mock_response)

    api_url = "https://api.example.com/data"
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        task_func(api_url)

    assert "HTTP error occurred: status code 404" in str(excinfo.value)

def test_task_func_with_empty_api_response(mocker):
    # Mock an empty API response
    mock_json_data = {}
    mock_response = MockResponse(mock_json_data, 200)
    mocker.patch('requests.get', return_value=mock_response)

    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)

    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert plot is None

def test_task_func_with_non_string_api_url():
    with pytest.raises(TypeError) as excinfo:
        task_func(12345)

    assert "api_url must be a string" in str(excinfo.value)