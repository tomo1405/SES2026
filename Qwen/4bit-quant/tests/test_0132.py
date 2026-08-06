import base64
import binascii

import pytest
from src_0132 import task_func


def test_task_func():
    # Test with a simple hex string and salt size
    hex_str = "616263"  # Represents "abc"
    salt_size = 4

    # Call the function
    result = task_func(hex_str, salt_size)

    # Check that the result is a tuple of two strings
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Decode the base64 encoded salt to check its length
    decoded_salt = base64.b64decode(result[0])
    assert len(decoded_salt) == salt_size

    # Verify that the hash value is a hexadecimal string of length 64
    assert len(result[1]) == 64
    assert all(c in '0123456789abcdef' for c in result[1])

def test_task_func_with_zero_salt():
    # Test with zero salt size
    hex_str = "616263"  # Represents "abc"
    salt_size = 0

    # Call the function
    result = task_func(hex_str, salt_size)

    # Check that the result is a tuple of two strings
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Decode the base64 encoded salt to check its length
    decoded_salt = base64.b64decode(result[0])
    assert len(decoded_salt) == salt_size

    # Verify that the hash value is a hexadecimal string of length 64
    assert len(result[1]) == 64
    assert all(c in '0123456789abcdef' for c in result[1])

def test_task_func_with_large_salt():
    # Test with a large salt size
    hex_str = "616263"  # Represents "abc"
    salt_size = 1024

    # Call the function
    result = task_func(hex_str, salt_size)

    # Check that the result is a tuple of two strings
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Decode the base64 encoded salt to check its length
    decoded_salt = base64.b64decode(result[0])
    assert len(decoded_salt) == salt_size

    # Verify that the hash value is a hexadecimal string of length 64
    assert len(result[1]) == 64
    assert all(c in '0123456789abcdef' for c in result[1])

def test_task_func_with_invalid_hex():
    # Test with an invalid hex string
    hex_str = "invalid_hex"  # Invalid hex string
    salt_size = 4

    with pytest.raises(binascii.Error):
        task_func(hex_str, salt_size)

def test_task_func_with_empty_hex():
    # Test with an empty hex string
    hex_str = ""  # Empty hex string
    salt_size = 4

    # Call the function
    result = task_func(hex_str, salt_size)

    # Check that the result is a tuple of two strings
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Decode the base64 encoded salt to check its length
    decoded_salt = base64.b64decode(result[0])
    assert len(decoded_salt) == salt_size

    # Verify that the hash value is a hexadecimal string of length 64
    assert len(result[1]) == 64
    assert all(c in '0123456789abcdef' for c in result[1])