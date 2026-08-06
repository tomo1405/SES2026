import pytest
from src_0341 import task_func

def test_task_func():
    # Test case 1: Valid request data
    req_data = {'name': 'John Doe', 'age': 30}
    expected_blake3_hex = '0x1234567890abcdef'
    expected_md5_hash = '0x1234567890abcdef'
    assert task_func(req_data) == (expected_blake3_hex, expected_md5_hash)

    # Test case 2: Invalid request data (non-string key)
    req_data = {'name': 'John Doe', 30: 'age'}
    with pytest.raises(TypeError):
        task_func(req_data)

    # Test case 3: Invalid request data (non-string value)
    req_data = {'name': 'John Doe', 'age': 30.5}
    with pytest.raises(TypeError):
        task_func(req_data)

    # Test case 4: Invalid request data (non-JSON serializable)
    req_data = {'name': 'John Doe', 'age': object()}
    with pytest.raises(TypeError):
        task_func(req_data)

    # Test case 5: Invalid request data (non-UTF-8 string)
    req_data = {'name': 'John Doe', 'age': '30'.encode('utf-16')}
    with pytest.raises(UnicodeEncodeError):
        task_func(req_data)