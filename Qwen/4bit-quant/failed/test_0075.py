import pytest
from src_0075 import task_func
import requests
import socket

def test_task_func_valid_host(mocker):
    mock_gethostbyname = mocker.patch('socket.gethostbyname', return_value='127.0.0.1')
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'city': 'New York', 'region': 'NY'}
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    
    result = task_func('example.com')
    
    mock_gethostbyname.assert_called_once_with('example.com')
    mock_get.assert_called_once_with('https://ipinfo.io/127.0.0.1')
    assert result == {
        'ip_address': '127.0.0.1',
        'geolocation': {'city': 'New York', 'region': 'NY'}
    }

def test_task_func_empty_host():
    with pytest.raises(ValueError, match="Host must be a non-empty string."):
        task_func('')

def test_task_func_socket_error(mocker):
    mocker.patch('socket.gethostbyname', side_effect=socket.gaierror)
    
    with pytest.raises(ConnectionError, match="Failed to retrieve information for example.com: "):
        task_func('example.com')

def test_task_func_requests_error(mocker):
    mock_gethostbyname = mocker.patch('socket.gethostbyname', return_value='127.0.0.1')
    mock_get = mocker.patch('requests.get')
    mock_get.side_effect = requests.HTTPError
    
    with pytest.raises(ConnectionError, match="Failed to retrieve information for example.com: "):
        task_func('example.com')