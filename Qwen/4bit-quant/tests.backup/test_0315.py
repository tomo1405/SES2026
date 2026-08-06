import pytest
from src_0315 import task_func

def test_task_func():
    # Mocking the socket and ssl modules to avoid actual network calls
    import mock

    # Define the expected response
    expected_response = "Mocked Response"

    # Mock the socket connection and SSL wrapping
    with mock.patch('socket.create_connection') as mock_socket, \
         mock.patch('ssl.create_default_context') as mock_ssl_context, \
         mock.patch('http.client.HTTPSConnection') as mock_https_connection:

        # Mock the socket object
        mock_sock = mock.Mock()
        mock_socket.return_value.__enter__.return_value = mock_sock

        # Mock the SSL context
        mock_context = mock.Mock()
        mock_ssl_context.return_value.wrap_socket.return_value = mock_sock

        # Mock the HTTPSConnection object
        mock_conn = mock.Mock()
        mock_https_connection.return_value.__enter__.return_value = mock_conn

        # Mock the response
        mock_response = mock.Mock()
        mock_conn.getresponse.return_value.read.return_value.decode.return_value = expected_response

        # Call the function
        result = task_func("example.com", 443, "/")

        # Assert the result
        assert result == expected_response

        # Assert that the methods were called correctly
        mock_socket.assert_called_once_with(("example.com", 443))
        mock_ssl_context.assert_called_once()
        mock_ssl_context.return_value.wrap_socket.assert_called_once_with(mock_sock, server_hostname="example.com")
        mock_https_connection.assert_called_once_with("example.com", 443, context=mock_ssl_context.return_value)
        mock_conn.request.assert_called_once_with('GET', '/')
        mock_conn.getresponse.assert_called_once()
        mock_response.read.assert_called_once()
        mock_response.read.return_value.decode.assert_called_once()