import pytest
from src_0132 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    hex_str = "48656c6c6f20576f726c64"
    salt_size = 16
    expected_output = ('c2FhZGVkIGZvciBteSBhY2NvdW50', 'a89ab3a9e54d9b5e0b857d9b4c84c9f56834e5a3')
    result = task_func(hex_str, salt_size)
    assert result == expected_output

    # Add more test cases as needed