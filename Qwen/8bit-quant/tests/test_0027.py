import pytest
from src_0027 import task_func

def test_task_func():
    # Test with a simple message and key
    message = "Hello, World!"
    encryption_key = "secret_key"
    expected_output = "gAAAAABiR4..."
    assert task_func(message, encryption_key) == expected_output

    # Test with an empty message
    message = ""
    encryption_key = "secret_key"
    expected_output = "gAAAAABiR4..."
    assert task_func(message, encryption_key) == expected_output

    # Test with a different message and key
    message = "Pytest is great!"
    encryption_key = "another_key"
    expected_output = "gAAAAABiR4..."
    assert task_func(message, encryption_key) == expected_output

    # Test with special characters in the message
    message = "!@#$%^&*()"
    encryption_key = "special_chars"
    expected_output = "gAAAAABiR4..."
    assert task_func(message, encryption_key) == expected_output

    # Test with a long message
    message = "a" * 1000
    encryption_key = "long_message_key"
    expected_output = "gAAAAABiR4..."
    assert task_func(message, encryption_key) == expected_output

    # Test with a long encryption key
    encryption_key = "a" * 32
    message = "Long Key Test"
    expected_output = "gAAAAABiR4..."
    assert task_func(message, encryption_key) == expected_output

# Note: The expected outputs in the assertions are placeholders.
# You should replace them with the actual expected outputs after running the tests.