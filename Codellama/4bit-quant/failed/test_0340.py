import pytest
from src_0340 import task_func

def test_task_func():
    # Test case 1: req_data is a dictionary
    req_data = {"key1": "value1", "key2": "value2"}
    secret_key = "my_secret_key"
    expected_signature = "1234567890abcdef"
    assert task_func(req_data, secret_key) == expected_signature

    # Test case 2: req_data is not a dictionary
    req_data = "not a dictionary"
    secret_key = "my_secret_key"
    with pytest.raises(TypeError):
        task_func(req_data, secret_key)

    # Test case 3: secret_key is not a string
    req_data = {"key1": "value1", "key2": "value2"}
    secret_key = 1234
    with pytest.raises(TypeError):
        task_func(req_data, secret_key)

    # Test case 4: req_data is empty
    req_data = {}
    secret_key = "my_secret_key"
    expected_signature = ""
    assert task_func(req_data, secret_key) == expected_signature

    # Test case 5: req_data has nested dictionaries
    req_data = {"key1": {"nested_key1": "nested_value1"}, "key2": "value2"}
    secret_key = "my_secret_key"
    expected_signature = "1234567890abcdef"
    assert task_func(req_data, secret_key) == expected_signature