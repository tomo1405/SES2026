import pytest
from unittest.mock import patch, MagicMock
from src_1040 import task_func

def test_task_func_file_exists():
    # Mocking SSLContext and socket
    with patch('src_1040.ssl.SSLContext') as mock_ssl_context, \
         patch('src_1040.os.path.exists') as mock_os_path_exists, \
         patch('src_1040.open', new_callable=patch.open) as mock_open, \
         patch('src_1040.hashlib.sha256') as mock_sha256:
        
        # Create a mock SSLContext object
        mock_context = MagicMock()
        mock_ssl_context.return_value = mock_context
        
        # Mock the wrap_socket method to return a mock secure socket
        mock_secure_socket = MagicMock()
        mock_context.wrap_socket.return_value = mock_secure_socket
        
        # Mock the receive data method to return a valid file path
        mock_secure_socket.recv.return_value = b'/path/to/file'
        
        # Mock the file content and SHA256 hash calculation
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.side_effect = [b'data1', b'data2', b'']
        mock_hash_object = mock_sha256.return_value
        mock_hash_object.hexdigest.return_value = 'expected_hash'
        
        # Set the mock to return True when checking if the file exists
        mock_os_path_exists.return_value = True
        
        # Call the function
        result = task_func(mock_secure_socket, 'cert_file', 'key_file')
        
        # Assert the expected result
        assert result == 'expected_hash'

def test_task_func_file_not_found():
    # Mocking SSLContext and socket
    with patch('src_1040.ssl.SSLContext') as mock_ssl_context, \
         patch('src_1040.os.path.exists') as mock_os_path_exists, \
         patch('src_1040.socket.socket') as mock_socket:
        
        # Create a mock SSLContext object
        mock_context = MagicMock()
        mock_ssl_context.return_value = mock_context
        
        # Mock the wrap_socket method to return a mock secure socket
        mock_secure_socket = MagicMock()
        mock_context.wrap_socket.return_value = mock_secure_socket
        
        # Mock the receive data method to return a non-existent file path
        mock_secure_socket.recv.return_value = b'/path/to/nonexistentfile'
        
        # Set the mock to return False when checking if the file exists
        mock_os_path_exists.return_value = False
        
        # Call the function
        result = task_func(mock_secure_socket, 'cert_file', 'key_file')
        
        # Assert the expected result
        assert result == 'File not found'

def test_task_func_exception_handling():
    # Mocking SSLContext and socket
    with patch('src_1040.ssl.SSLContext') as mock_ssl_context, \
         patch('src_1040.os.path.exists') as mock_os_path_exists, \
         patch('src_1040.socket.socket') as mock_socket:
        
        # Create a mock SSLContext object
        mock_context = MagicMock()
        mock_ssl_context.return_value = mock_context
        
        # Mock the wrap_socket method to return a mock secure socket
        mock_secure_socket = MagicMock()
        mock_context.wrap_socket.return_value = mock_secure_socket
        
        # Mock the receive data method to raise an exception
        mock_secure_socket.recv.side_effect = Exception('Mocked exception')
        
        # Set the mock to return True when checking if the file exists
        mock_os_path_exists.return_value = True
        
        # Call the function
        result = task_func(mock_secure_socket, 'cert_file', 'key_file')
        
        # Assert the expected result
        assert result == 'Error: Mocked exception'