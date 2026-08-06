import pytest
from src_0505 import task_func

# Mocking dependencies
from unittest.mock import mock_open, patch

# Constants
MOCK_FILE_PATH = 'mock_file_path'
MOCK_CONTENT = b'mock_content'
MOCK_PRIVATE_KEY_PATH = 'private.pem'
MOCK_PRIVATE_KEY = b'mock_private_key'

def test_task_func():
    # Mock reading the file content
    m = mock_open(read_data=MOCK_CONTENT)
    with patch('builtins.open', m):
        # Mock reading the private key
        with patch('src_0505.open', mock_open(read_data=MOCK_PRIVATE_KEY), create=True) as mocked_key_file:
            # Mock the rsa.sign function to return a known signature
            with patch('src_0505.rsa.sign', return_value=b'mock_signature'):
                # Call the function
                result = task_func(MOCK_FILE_PATH)

    # Assertions
    assert result == 'bW9ja19zaWduYXR1cmU='  # Base64 encoded 'mock_signature'

    # Check if files were opened correctly
    m.assert_called_once_with(MOCK_FILE_PATH, 'rb')
    mocked_key_file.assert_called_once_with(MOCK_PRIVATE_KEY_PATH, 'rb')