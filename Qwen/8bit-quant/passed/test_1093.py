import pytest
from src_1093 import task_func
import requests
from bs4 import BeautifulSoup
from unittest.mock import patch

def test_task_func_valid_url():
    url = "https://example.com"
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "<html><body><script>['valid', 'json']</script></body></html>"
        result = task_func(url)
        assert result == [['valid', 'json']]

def test_task_func_invalid_json():
    url = "https://example.com"
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "<html><body><script>invalid json</script></body></html>"
        result = task_func(url)
        assert result == []

def test_task_func_no_scripts():
    url = "https://example.com"
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "<html><body></body></html>"
        result = task_func(url)
        assert result == []

def test_task_func_request_exception():
    url = "https://example.com"
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException
        result = task_func(url)
        assert result == []

def test_task_func_empty_response():
    url = "https://example.com"
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = ""
        result = task_func(url)
        assert result == []

def test_task_func_multiple_scripts():
    url = "https://example.com"
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "<html><body><script>['valid1', 'json1']</script><script>['valid2', 'json2']</script></body></html>"
        result = task_func(url)
        assert result == [['valid1', 'json1'], ['valid2', 'json2']]