import pytest
from src_0315 import task_func

# Mocking the necessary modules and classes
from unittest.mock import patch, MagicMock

@patch('src_0315.ssl.create_default_context')
@patch('src_0315.socket.create_connection')
@patch('src_0315.http.client.HTTPSConnection')
def test_task_func(mock_https_conn, mock_create_connection, mock_create_default_context):
    # Setup mock objects
    mock_context = MagicMock()
    mock_sock = MagicMock()
    mock_ssock = MagicMock()
    mock_response = MagicMock()
    mock_conn = MagicMock()

    # Configure mocks
    mock_create_default_context.return_value = mock_context
    mock_create_connection.return_value = mock_sock
    mock_context.wrap_socket.return_value = mock_ssock
    mock_https_conn.return_value = mock_conn
    mock_conn.getresponse.return_value = mock_response
    mock_response.read.return_value = b'{"key": "value"}'

    # Test data
    server_name = 'example.com'
    server_port = 443
    path = '/api/data'

    # Call the function
    result = task_func(server_name, server_port, path)

    # Assertions
    mock_create_default_context.assert_called_once()
    mock_create_connection.assert_called_once_with((server_name, server_port))
    mock_context.wrap_socket.assert_called_once_with(mock_sock, server_hostname=server_name)
    mock_https_conn.assert_called_once_with(server_name, server_port, context=mock_context)
    mock_conn.request.assert_called_once_with('GET', path)
    mock_conn.getresponse.assert_called_once()
    mock_response.read.assert_called_once()
    assert result == '{"key": "value"}'