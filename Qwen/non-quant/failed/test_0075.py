import pytest
from src_0075 import task_func
from unittest.mock import patch, Mock

def test_task_func_with_valid_host():
    with patch('socket.gethostbyname', return_value='127.0.0.1'):
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {'city': 'TestCity', 'region': 'TestRegion'}
            mock_get.return_value = mock_response

            result = task_func('example.com')
            assert result == {
                'ip_address': '127.0.0.1',
                'geolocation': {'city': 'TestCity', 'region': 'TestRegion'}
            }

def test_task_func_with_empty_host():
    with pytest.raises(ValueError, match="Host must be a non-empty string."):
        task_func('')

def test_task_func_with_invalid_host():
    with patch('socket.gethostbyname', side_effect=socket.gaierror):
        with pytest.raises(ConnectionError, match="Failed to retrieve information for example.com: "):
            task_func('example.com')

def test_task_func_with_http_error():
    with patch('socket.gethostbyname', return_value='127.0.0.1'):
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            with pytest.raises(ConnectionError, match="Failed to retrieve information for example.com: "):
                task_func('example.com')