import pytest
from unittest.mock import patch
from src_0033 import task_func

def test_task_func_valid_url_and_tag():
    with patch('requests.get') as mock_get:
        mock_response = type('Response', (object,), {'text': '<html><body><h1>Test</h1></body></html>'})
        mock_get.return_value = mock_response
        result = task_func('http://example.com', 'h1')
        assert result == 'Test'

def test_task_func_invalid_url():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException
        result = task_func('http://nonexistenturl.com', 'h1')
        assert result is None

def test_task_func_tag_not_found():
    with patch('requests.get') as mock_get:
        mock_response = type('Response', (object,), {'text': '<html><body></body></html>'})
        mock_get.return_value = mock_response
        result = task_func('http://example.com', 'p')
        assert result is None

def test_task_func_no_content_in_tag():
    with patch('requests.get') as mock_get:
        mock_response = type('Response', (object,), {'text': '<html><body><h1></h1></body></html>'})
        mock_get.return_value = mock_response
        result = task_func('http://example.com', 'h1')
        assert result is None