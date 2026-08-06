import pytest
from unittest.mock import Mock, patch
from src_1040 import task_func

def test_task_func_file_exists():
    # Arrange
    client_socket = Mock()
    client_socket.recv.return_value = b"/path/to/existing/file"
    cert_file = "path/to/cert.pem"
    key_file = "path/to/key.pem"
    mock_open = Mock()
    mock_file = Mock()
    mock_file.read.side_effect = [b"data", b""]
    mock_open.return_value.__enter__.return_value = mock_file
    with patch('src_1040.os.path.exists', return_value=True), \
         patch('src_1040.open', mock_open), \
         patch('src_1040.ssl.SSLContext') as mock_ssl_context:
        mock_context = Mock()
        mock_ssl_context.wrap_socket.return_value = client_socket
        mock_ssl_context.load_cert_chain = Mock()
        context_instance = mock_ssl_context.return_value
        context_instance.wrap_socket = mock_context.wrap_socket

        # Act
        response = task_func(client_socket, cert_file, key_file)

        # Assert
        assert response == hashlib.sha256(b"data").hexdigest()
        client_socket.send.assert_called_once_with(hashlib.sha256(b"data").hexdigest().encode("utf-8"))

def test_task_func_file_not_exists():
    # Arrange
    client_socket = Mock()
    client_socket.recv.return_value = b"/path/to/nonexistent/file"
    cert_file = "path/to/cert.pem"
    key_file = "path/to/key.pem"
    with patch('src_1040.os.path.exists', return_value=False), \
         patch('src_1040.ssl.SSLContext') as mock_ssl_context:
        mock_context = Mock()
        mock_context.wrap_socket.return_value = client_socket
        mock_context.load_cert_chain = Mock()
        context_instance = mock_ssl_context.return_value
        context_instance.wrap_socket = mock_context.wrap_socket

        # Act
        response = task_func(client_socket, cert_file, key_file)

        # Assert
        assert response == "File not found"
        client_socket.send.assert_called_once_with("File not found".encode("utf-8"))

def test_task_func_exception():
    # Arrange
    client_socket = Mock()
    client_socket.recv.side_effect = Exception("Mocked exception")
    cert_file = "path/to/cert.pem"
    key_file = "path/to/key.pem"
    with patch('src_1040.ssl.SSLContext') as mock_ssl_context:
        mock_context = Mock()
        mock_context.wrap_socket.return_value = client_socket
        mock_context.load_cert_chain = Mock()
        context_instance = mock_ssl_context.return_value
        context_instance.wrap_socket = mock_context.wrap_socket

        # Act
        response = task_func(client_socket, cert_file, key_file)

        # Assert
        assert response == "Error: Mocked exception"
        client_socket.send.assert_called_once_with("Error: Mocked exception".encode("utf-8"))