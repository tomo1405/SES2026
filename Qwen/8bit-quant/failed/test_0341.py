import pytest
from src_0341 import task_func
import json
import hashlib
import blake3

def test_task_func():
    # Test case 1: Simple dictionary
    req_data = {"key": "value"}
    expected_blake3_hex = "a1d0c6e83f027327d8461063f4ac58a6"
    expected_md5_hash = "b10a8db164e0754105b7a99be72e3fe5"
    
    blake3_hex, md5_hash = task_func(req_data)
    assert blake3_hex == expected_blake3_hex
    assert md5_hash == expected_md5_hash

    # Test case 2: Empty dictionary
    req_data = {}
    expected_blake3_hex = "af1349b9f1d4c8e9b9f1d4c8e9b9f1d4"
    expected_md5_hash = "d41d8cd98f00b204e9800998ecf8427e"
    
    blake3_hex, md5_hash = task_func(req_data)
    assert blake3_hex == expected_blake3_hex
    assert md5_hash == expected_md5_hash

    # Test case 3: Nested dictionary
    req_data = {"nested": {"key": "value"}}
    expected_blake3_hex = "b1d0c6e83f027327d8461063f4ac58a6"
    expected_md5_hash = "b10a8db164e0754105b7a99be72e3fe5"
    
    blake3_hex, md5_hash = task_func(req_data)
    assert blake3_hex == expected_blake3_hex
    assert md5_hash == expected_md5_hash

    # Test case 4: List of dictionaries
    req_data = [{"key": "value"}, {"another_key": "another_value"}]
    expected_blake3_hex = "c1d0c6e83f027327d8461063f4ac58a6"
    expected_md5_hash = "b10a8db164e0754105b7a99be72e3fe5"
    
    blake3_hex, md5_hash = task_func(req_data)
    assert blake3_hex == expected_blake3_hex
    assert md5_hash == expected_md5_hash

    # Test case 5: String input
    req_data = "test_string"
    expected_blake3_hex = "e1d0c6e83f027327d8461063f4ac58a6"
    expected_md5_hash = "b10a8db164e0754105b7a99be72e3fe5"
    
    blake3_hex, md5_hash = task_func(req_data)
    assert blake3_hex == expected_blake3_hex
    assert md5_hash == expected_md5_hash