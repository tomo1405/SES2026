import binascii

import pytest
from src_0413 import task_func


def test_task_func_valid_json():
    # Create a temporary JSON file with encoded data
    json_content = '{"key1": "SGVsbG8gV29ybGQh", "key2": "UHl0aG9uIQ=="}'
    with open('test_data.json', 'w') as f:
        f.write(json_content)
    
    # Expected output after decoding
    expected_output = {
        'key1': 'Hello World!',
        'key2': 'Python!'
    }
    
    # Call the function and assert the result
    result = task_func('test_data.json')
    assert result == expected_output

def test_task_func_invalid_base64():
    # Create a temporary JSON file with invalid base64 data
    json_content = '{"key1": "invalid_base64"}'
    with open('test_data_invalid.json', 'w') as f:
        f.write(json_content)
    
    # Test should raise an exception due to invalid base64
    with pytest.raises((UnicodeDecodeError, binascii.Error)):
        task_func('test_data_invalid.json')

def test_task_func_nonexistent_file():
    # Test should raise an exception if the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_file.json')

def test_task_func_empty_json():
    # Create a temporary empty JSON file
    json_content = '{}'
    with open('empty_data.json', 'w') as f:
        f.write(json_content)
    
    # Expected output for empty JSON
    expected_output = {}
    
    # Call the function and assert the result
    result = task_func('empty_data.json')
    assert result == expected_output