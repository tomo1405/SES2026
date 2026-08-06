import json
from unittest.mock import patch

import pytest
import requests
from src_1136 import task_func


def test_task_func_success():
    # Mock the response from requests.get
    class MockResponse:
        def __init__(self, text):
            self.text = text

    mock_data = '''
    [
        {"name": "repo1", "created_at": "2020-01-01T00:00:00Z"},
        {"name": "repo2", "created_at": "2019-01-01T00:00:00Z"},
        {"name": "repo3", "created_at": "2021-01-01T00:00:00Z"}
    ]
    '''
    with patch('requests.get', return_value=MockResponse(mock_data)):
        result = task_func('test_user')
        assert result == ['repo2', 'repo1', 'repo3']

def test_task_func_no_repos():
    # Mock the response from requests.get
    class MockResponse:
        def __init__(self, text):
            self.text = text

    mock_data = '[]'
    with patch('requests.get', return_value=MockResponse(mock_data)):
        result = task_func('test_user')
        assert result == []

def test_task_func_connection_error():
    # Mock the response from requests.get to raise an exception
    with patch('requests.get', side_effect=requests.exceptions.RequestException):
        with pytest.raises(requests.exceptions.RequestException):
            task_func('test_user')

def test_task_func_invalid_json():
    # Mock the response from requests.get with invalid JSON
    class MockResponse:
        def __init__(self, text):
            self.text = text

    mock_data = '{"invalid": json}'
    with patch('requests.get', return_value=MockResponse(mock_data)):
        with pytest.raises(json.JSONDecodeError):
            task_func('test_user')