import pytest
from src_0341 import task_func

def test_task_func():
    # Test case 1: Basic input
    req_data = {"key": "value"}
    expected_blake3_hex = "b'\\x00' * 64"
    expected_md5_hash = "d41d8cd98f00b204e9800998ecf8427e"
    blake3_hex, md5_hash = task_func(req_data)
    assert blake3_hex == expected_blake3_hex
    assert md5_hash == expected_md5_hash

    # Add more test cases as needed