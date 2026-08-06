import pytest
from unittest.mock import Mock, patch
from src_1040 import task_func

def test_task_func_file_exists():
    # Mock the client socket and file operations
    mock_client_socket = Mock()
    mock_client_socket.recv.return_value = b"test_file.txt"
    
    mock_file = Mock()
    mock_file.read.side_effect = [b"data", b""]
    
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', return_value=mock_file):
            with patch('ssl.SSLContext') as MockSSLContext:
                mock_context = MockSSLContext.return_value
                mock_context.wrap_socket.return_value = mock_client_socket
                
                response = task_func(mock_client_socket, "cert.pem", "key.pem")
                
                assert response == "d5503c8a1d5e6e2d8a3d7f2a1e2e2e2e2e2e2e2e2e2e2e2e2e2e2e2e2e2e2e2e"

def test_task_func_file_not_exists():
    # Mock the client socket and file operations
    mock_client_socket = Mock()
    mock_client_socket.recv.return_value = b"nonexistent_file.txt"
    
    with patch('os.path.exists', return_value=False):
        with patch('ssl.SSLContext') as MockSSLContext:
            mock_context = MockSSLContext.return_value
            mock_context.wrap_socket.return_value = mock_client_socket
            
            response = task_func(mock_client_socket, "cert.pem", "key.pem")
            
            assert response == "File not found"

def test_task_func_exception():
    # Mock the client socket and file operations
    mock_client_socket = Mock()
    mock_client_socket.recv.return_value = b"test_file.txt"
    
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', side_effect=IOError):
            with patch('ssl.SSLContext') as MockSSLContext:
                mock_context = MockSSLContext.return_value
                mock_context.wrap_socket.return_value = mock_client_socket
                
                response = task_func(mock_client_socket, "cert.pem", "key.pem")
                
                assert response.startswith("Error: ")