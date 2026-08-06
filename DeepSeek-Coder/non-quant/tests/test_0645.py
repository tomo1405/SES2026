import pytest
from src_0645 import task_func
import os
import hashlib
import base64

# Test cases for the task_func function

def test_task_func():
    # Test with a simple case
    filename = "test_file.txt"
    data = "Hello, World!"
    password = "secret"
    expected_encrypted = "SGVsbG8sIFdvcmxkIQ=="  # Expected base64 encoded encrypted data

    # Call the function
    result = task_func(filename, data, password)

    # Read the file and check the content
    with open(filename, 'r') as f:
        encrypted_content = f.read()

    # Clean up
    os.remove(filename)

    assert result == expected_encrypted
    assert encrypted_content == expected_encrypted

# Add more test cases as needed