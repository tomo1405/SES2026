import pytest
from src_0340 import task_func

def test_task_func_valid_input():
    req_data = {"key1": "value1", "key2": "value2"}
    secret_key = "my_secret_key"
    expected_output = "1234567890abcdef"

    output = task_func(req_data, secret_key)

    assert output == expected_output

def test_task_func_invalid_input():
    req_data = "invalid_input"
    secret_key = "my_secret_key"

    with pytest.raises(TypeError):
        task_func(req_data, secret_key)