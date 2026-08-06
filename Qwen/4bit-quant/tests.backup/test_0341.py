import pytest
from src_0341 import task_func

def test_task_func():
    # Test with a simple dictionary
    req_data = {"key": "value"}
    blake3_hex, md5_hash = task_func(req_data)
    assert isinstance(blake3_hex, str)
    assert isinstance(md5_hash, str)
    
    # Test with a more complex dictionary
    req_data = {"name": "John", "age": 30, "city": "New York"}
    blake3_hex, md5_hash = task_func(req_data)
    assert isinstance(blake3_hex, str)
    assert isinstance(md5_hash, str)

    # Test with an empty dictionary
    req_data = {}
    blake3_hex, md5_hash = task_func(req_data)
    assert isinstance(blake3_hex, str)
    assert isinstance(md5_hash, str)

    # Test with a list
    req_data = [1, 2, 3, 4]
    blake3_hex, md5_hash = task_func(req_data)
    assert isinstance(blake3_hex, str)
    assert isinstance(md5_hash, str)

    # Test with nested structures
    req_data = {"user": {"name": "Alice", "age": 25}, "items": [1, 2, 3]}
    blake3_hex, md5_hash = task_func(req_data)
    assert isinstance(blake3_hex, str)
    assert isinstance(md5_hash, str)