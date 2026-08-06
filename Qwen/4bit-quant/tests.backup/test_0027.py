import pytest
from src_0027 import task_func

def test_task_func():
    # Test with a simple message and key
    message = "Hello, World!"
    encryption_key = "mysecretkey123"
    encrypted_message = task_func(message, encryption_key)
    
    # Check if the output is a string
    assert isinstance(encrypted_message, str), "The output should be a string"
    
    # Check if the output is not equal to the original message
    assert encrypted_message != message, "The encrypted message should not be the same as the original message"

    # Check with an empty message
    message_empty = ""
    encrypted_message_empty = task_func(message_empty, encryption_key)
    assert encrypted_message_empty == "", "The encrypted message for an empty string should be an empty string"

    # Check with a different key
    encryption_key_diff = "anotherkey456"
    encrypted_message_diff = task_func(message, encryption_key_diff)
    assert encrypted_message_diff != encrypted_message, "The encrypted message with a different key should be different"

    # Check with a non-ASCII character
    message_unicode = "こんにちは, 世界!"
    encrypted_message_unicode = task_func(message_unicode, encryption_key)
    assert isinstance(encrypted_message_unicode, str), "The output should be a string even with non-ASCII characters"
    assert encrypted_message_unicode != message_unicode, "The encrypted message should not be the same as the original message with non-ASCII characters"