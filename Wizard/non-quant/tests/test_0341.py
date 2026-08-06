python
import json
import hashlib
import blake3
import pytest

def task_func(req_data):
    # Convert request data to json string
    json_req_data = json.dumps(req_data)
    # Hash the request data using BLAKE3 and get hexadecimal representation directly
    blake3_hex = blake3.blake3(json_req_data.encode('utf-8')).hexdigest()
    # Use hashlib for generating an MD5 hash of the BLAKE3 hex representation (for demonstration)
    md5_hash = hashlib.md5(blake3_hex.encode('utf-8')).hexdigest()

    return blake3_hex, md5_hash

def test_task_func():
    # Test case 1
    req_data = {'name': 'John', 'age': 30}
    expected_blake3_hex = '7a1a7d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d'
    expected_md5_hash = '7a1a7d5d5d5d5d5d5d5d5d5d5d5d5d5d'
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)

    # Test case 2
    req_data = {'name': 'Jane', 'age': 25}
    expected_blake3_hex = '7a1a7d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d'
    expected_md5_hash = '7a1a7d5d5d5d5d5d5d5d5d5d5d5d5d5d'
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)

    # Test case 3
    req_data = {'name': 'Bob', 'age': 40}
    expected_blake3_hex = '7a1a7d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d'
    expected_md5_hash = '7a1a7d5d5d5d5d5d5d5d5d5d5d5d5d5d'
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)