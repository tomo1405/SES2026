import json
import os
from unittest.mock import mock_open, patch

import pytest
import requests
from src_0403 import task_func


@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self, text):
            self.text = text

    return MockResponse(json.dumps({'data': ['item1', 'item2']}))

@patch('src_0403.requests.get')
@patch('src_0403.open', new_callable=mock_open)
def test_task_func(mock_open, mock_get, mock_response):
    # Mock the API response
    mock_get.return_value = mock_response

    # Define the pattern to search for
    pattern = 'i'

    # Call the function
    result = task_func(pattern)

    # Check that the CSV file was written correctly
    mock_open.assert_called_once_with('matched_data.csv', 'w')
    handle = mock_open()
    handle().writerows.assert_called_once_with([['i'], ['i']])

    # Check that the function returns the correct path
    assert result == os.path.abspath('matched_data.csv')

@patch('src_0403.requests.get')
def test_task_func_api_failure(mock_get):
    # Mock the API response to simulate a failure
    mock_get.side_effect = requests.exceptions.RequestException

    # Define the pattern to search for
    pattern = 'i'

    # Call the function and check that it raises an exception
    with pytest.raises(requests.exceptions.RequestException):
        task_func(pattern)