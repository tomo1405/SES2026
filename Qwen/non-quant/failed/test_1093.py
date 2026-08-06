import pytest
from src_1093 import task_func
from unittest.mock import patch
from bs4 import BeautifulSoup

def test_task_func_success():
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'<html><head><script>{"key": "value"}</script></head></html>'

    with patch('requests.get', return_value=mock_response):
        result = task_func('http://example.com')
        assert result == [{'key': 'value'}]

def test_task_func_no_scripts():
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'<html><head></head></html>'

    with patch('requests.get', return_value=mock_response):
        result = task_func('http://example.com')
        assert result == []

def test_task_func_invalid_script():
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'<html><head><script>invalid</script></head></html>'

    with patch('requests.get', return_value=mock_response):
        result = task_func('http://example.com')
        assert result == []

def test_task_func_request_exception():
    with patch('requests.get', side_effect=requests.RequestException):
        result = task_func('http://example.com')
        assert result == []

def test_task_func_non_200_status():
    mock_response = requests.Response()
    mock_response.status_code = 404

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(requests.RequestException):
            task_func('http://example.com')