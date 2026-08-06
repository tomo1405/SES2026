import json
from unittest.mock import patch

import requests
from src_0190 import task_func


def test_task_func_valid_url():
    mock_data = {
        'names': ['Alice', 'Bob', 'Charlie']
    }
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(mock_data).encode('utf-8')

    with patch('requests.get', return_value=mock_response):
        result = task_func('http://example.com/data')
        assert result == ['Alice', 'Bob', 'Charlie']

def test_task_func_invalid_url():
    with patch('requests.get', side_effect=requests.exceptions.RequestException):
        result = task_func('http://invalid-url.com/data')
        assert result == "Invalid url input"

def test_task_func_missing_names_key():
    mock_data = {
        'other_key': ['Alice', 'Bob', 'Charlie']
    }
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(mock_data).encode('utf-8')

    with patch('requests.get', return_value=mock_response):
        result = task_func('http://example.com/data')
        assert result == []

def test_task_func_non_list_names_value():
    mock_data = {
        'names': 'Not a list'
    }
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(mock_data).encode('utf-8')

    with patch('requests.get', return_value=mock_response):
        result = task_func('http://example.com/data')
        assert result == []