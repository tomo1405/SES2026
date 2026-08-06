import pytest
from src_1015 import task_func
import requests
import pandas as pd

# Mocking the requests.get function
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError(f"HTTP {self.status_code} error")

def test_task_func_valid_api_url(mocker):
    # Mock the response from the API
    mock_json_data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    mock_response = MockResponse(mock_json_data, 200)
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function with a valid API URL
    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)

    # Check that the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert 'name' in df.columns
    assert 'age' in df.columns

    # Check that the plot is created
    assert plot is not None

def test_task_func_invalid_api_url():
    # Test with an invalid API URL (non-string type)
    with pytest.raises(TypeError, match="api_url must be a string"):
        task_func(12345)

def test_task_func_api_failure(mocker):
    # Mock the response from the API to simulate an HTTP error
    mock_response = MockResponse({}, 404)
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function with a valid API URL but expect an HTTP error
    api_url = "https://api.example.com/data"
    with pytest.raises(requests.exceptions.HTTPError, match="HTTP 404 error"):
        task_func(api_url)

def test_task_func_empty_response(mocker):
    # Mock the response from the API with an empty JSON array
    mock_json_data = []
    mock_response = MockResponse(mock_json_data, 200)
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function with a valid API URL but expect an empty DataFrame
    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)

    # Check that the DataFrame is empty
    assert isinstance(df, pd.DataFrame)
    assert df.empty

    # Check that no plot is created
    assert plot is None