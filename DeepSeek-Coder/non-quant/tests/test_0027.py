import pytest
from src_0027 import task_func

def test_task_func():
    # Test case 1: Basic encryption
    message = "Hello, World!"
    encryption_key = "secret_key"
    encrypted_message = task_func(message, encryption_key)
    assert isinstance(encrypted_message, str)

    # Additional assertions can be added to validate the encryption process

# Add more test cases as needed