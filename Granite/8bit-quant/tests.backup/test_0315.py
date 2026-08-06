import pytest
from src_0315 import task_func

def test_task_func():
    SERVER_NAME = 'example.com'
    SERVER_PORT = 443
    path = '/index.html'
    expected_output = b'Hello, world!'

    with patch('ssl.create_default_context') as mock_create_default_context:
        with patch('socket.create_connection') as mock_create_connection:
            with patch('http.client.HTTPSConnection') as mock_HTTPSConnection:
                mock_create_connection.return_value.recv.return_value = expected_output
                actual_output = task_func(SERVER_NAME, SERVER_PORT, path)
                assert actual_output == expected_output
                mock_create_default_context.assert_called_once()
                mock_create_connection.assert_called_once_with((SERVER_NAME, SERVER_PORT))
                mock_HTTPSConnection.assert_called_once_with(SERVER_NAME, SERVER_PORT, context=mock_create_default_context.return_value)
                mock_HTTPSConnection.return_value.request.assert_called_once_with('GET', path)
                mock_HTTPSConnection.return_value.getresponse.assert_called_once()
                mock_HTTPSConnection.return_value.getresponse.return_value.read.assert_called_once()
                mock_HTTPSConnection.return_value.getresponse.return_value.read.return_value.decode.assert_called_once()