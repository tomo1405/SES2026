import pytest
from src_1040 import task_func

def test_task_func():
    client_socket = None
    cert_file = "path/to/certfile"
    key_file = "path/to/keyfile"
    buffer_size = 1024

    # Test case 1: Valid request
    request = "path/to/file"
    expected_response = "expected_sha256_hash"
    with patch("ssl.SSLContext") as mock_ssl_context, patch("ssl.SSLSocket") as mock_ssl_socket, patch("os.path.exists") as mock_os_path_exists, patch("hashlib.sha256") as mock_sha256:
        mock_os_path_exists.return_value = True
        mock_ssl_socket.return_value = "secure_socket"
        mock_ssl_context.return_value = "context"
        mock_sha256.return_value = "sha256_hash"
        response = task_func(client_socket, cert_file, key_file, buffer_size)
        assert response == expected_response

    # Test case 2: Invalid request
    request = "invalid_request"
    expected_response = "File not found"
    with patch("ssl.SSLContext") as mock_ssl_context, patch("ssl.SSLSocket") as mock_ssl_socket, patch("os.path.exists") as mock_os_path_exists, patch("hashlib.sha256") as mock_sha256:
        mock_os_path_exists.return_value = False
        mock_ssl_socket.return_value = "secure_socket"
        mock_ssl_context.return_value = "context"
        mock_sha256.return_value = "sha256_hash"
        response = task_func(client_socket, cert_file, key_file, buffer_size)
        assert response == expected_response

    # Test case 3: Exception
    request = "path/to/file"
    expected_response = "Error: Some error message"
    with patch("ssl.SSLContext") as mock_ssl_context, patch("ssl.SSLSocket") as mock_ssl_socket, patch("os.path.exists") as mock_os_path_exists, patch("hashlib.sha256") as mock_sha256:
        mock_os_path_exists.return_value = True
        mock_ssl_socket.return_value = "secure_socket"
        mock_ssl_context.return_value = "context"
        mock_sha256.return_value = "sha256_hash"
        mock_ssl_socket.recv.side_effect = Exception("Some error message")
        response = task_func(client_socket, cert_file, key_file, buffer_size)
        assert response == expected_response