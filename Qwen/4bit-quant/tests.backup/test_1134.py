import pytest
from src_1134 import task_func
import requests
from unittest.mock import patch, Mock

@patch('src_1134.requests.get')
def test_task_func_success(mock_get):
    # Mock the response from requests.get
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'key': 'value'}
    mock_get.return_value = mock_response

    API_URL = "https://api.example.com"
    endpoint = "/data"
    PREFIX = "test_"

    # Call the function
    result = task_func(API_URL, endpoint, PREFIX)

    # Assert that the correct filename is returned
    assert result == "test_/data.json"

    # Assert that the file was written correctly
    with open("test_/data.json", 'r') as f:
        data = json.load(f)
        assert data == {'key': 'value'}

    # Clean up the created file
    import os
    os.remove("test_/data.json")

@patch('src_1134.requests.get')
def test_task_func_failure(mock_get):
    # Mock the response to simulate a request failure
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("HTTP Error")
    mock_get.return_value = mock_response

    API_URL = "https://api.example.com"
    endpoint = "/data"
    PREFIX = "test_"

    # Assert that a RuntimeError is raised
    with pytest.raises(RuntimeError) as excinfo:
        task_func(API_URL, endpoint, PREFIX)

    # Assert the error message
    assert str(excinfo.value) == "Error fetching data from API: HTTP Error"