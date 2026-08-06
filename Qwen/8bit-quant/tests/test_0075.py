import socket
from unittest.mock import Mock, patch

import pytest
from src_0075 import task_func


def test_task_func_with_valid_host():
    with patch('socket.gethostbyname', return_value='123.45.67.89'):
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {'city': 'Test City', 'region': 'Test Region'}
            mock_get.return_value = mock_response

            result = task_func('example.com')

            assert result == {
                'ip_address': '123.45.67.89',
                'geolocation': {'city': 'Test City', 'region': 'Test Region'}
            }

def test_task_func_with_empty_host():
    with pytest.raises(ValueError, match="Host must be a non-empty string."):
        task_func('')

def test_task_func_with_invalid_host():
    with patch('socket.gethostbyname', side_effect=socket.gaierror("Mocked gaierror")):
        with pytest.raises(ConnectionError, match="Failed to retrieve information for example.com: Mocked gaierror"):
            task_func('example.com')

def test_task_func_with_http_error():
    with patch('socket.gethostbyname', return_value='123.45.67.89'):
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            with pytest.raises(ConnectionError, match="Failed to retrieve information for example.com: 404 Client Error: None for url: https://ipinfo.io/123.45.67.89"):
                task_func('example.com')