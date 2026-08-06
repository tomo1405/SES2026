import pytest
from src_0341 import task_func
import json
import hashlib
import blake3

def test_task_func():
    # Test case 1: Simple dictionary
    req_data = {"key": "value"}
    expected_blake3_hex = blake3.blake3(json.dumps(req_data).encode('utf-8')).hexdigest()
    expected_md5_hash = hashlib.md5(expected_blake3_hex.encode('utf-8')).hexdigest()
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)

    # Test case 2: Empty dictionary
    req_data = {}
    expected_blake3_hex = blake3.blake3(json.dumps(req_data).encode('utf-8')).hexdigest()
    expected_md5_hash = hashlib.md5(expected_blake3_hex.encode('utf-8')).hexdigest()
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)

    # Test case 3: Nested dictionary
    req_data = {"outer": {"inner": "value"}}
    expected_blake3_hex = blake3.blake3(json.dumps(req_data).encode('utf-8')).hexdigest()
    expected_md5_hash = hashlib.md5(expected_blake3_hex.encode('utf-8')).hexdigest()
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)

    # Test case 4: List as value
    req_data = {"key": [1, 2, 3]}
    expected_blake3_hex = blake3.blake3(json.dumps(req_data).encode('utf-8')).hexdigest()
    expected_md5_hash = hashlib.md5(expected_blake3_hex.encode('utf-8')).hexdigest()
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)

    # Test case 5: String with special characters
    req_data = {"key": "!@#$%^&*()"}
    expected_blake3_hex = blake3.blake3(json.dumps(req_data).encode('utf-8')).hexdigest()
    expected_md5_hash = hashlib.md5(expected_blake3_hex.encode('utf-8')).hexdigest()
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)