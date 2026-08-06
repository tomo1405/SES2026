import pytest
from src_0131 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    salt_size = 16
    expected_output = ('c2FhZGVkIGZvciB0aGUgY2hhbGxlbmdlIG9mIHRoZSB0aW55IGFuZCB0aGUgY29uZ2VuaXRhc2l0eSBvZiB0aGUgZGV2ZWxvcG1lbnQ=', '8c6978a5e8e9b61e6a7a1d2f5e6d3b837f8f86b3f7e1e4b3c2d896c8f1f9b6b')
    result = task_func(hex_str, salt_size)
    assert result == expected_output

    # Add more test cases as needed