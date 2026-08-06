import pytest
from src_0506 import task_func

def test_task_func():
    # Test with a simple secret and message
    secret = "my_secret"
    message = "hello_world"
    expected_hash = "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"
    assert task_func(secret, message) == expected_hash

    # Test with different secret and message
    secret = "another_secret"
    message = "goodbye_world"
    expected_hash = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6"
    assert task_func(secret, message) == expected_hash

    # Test with empty secret and message
    secret = ""
    message = ""
    expected_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert task_func(secret, message) == expected_hash

    # Test with special characters in secret and message
    secret = "!@#$%^&*()"
    message = "1234567890"
    expected_hash = "3a6eb0b6e6b2e4b1e5b3e2b4e3b5e6b7e8b9e0b1e2b3e4b5e6b7e8b9e0b1e2b3"
    assert task_func(secret, message) == expected_hash

    # Test with Unicode characters in secret and message
    secret = "مرحبا"
    message = "العالم"
    expected_hash = "b5a8e6b7e8b9e0b1e2b3e4b5e6b7e8b9e0b1e2b3e4b5e6b7e8b9e0b1e2b3"
    assert task_func(secret, message) == expected_hash