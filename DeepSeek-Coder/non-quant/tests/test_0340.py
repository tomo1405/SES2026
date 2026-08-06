import pytest
from src_0340 import task_func

def test_task_func_valid_input():
    req_data = {"key": "value"}
    secret_key = "secret"
    result = task_func(req_data=req_data, secret_key=secret_key)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) > 0, "The result should not be empty"

def test_task_func_invalid_input():
    req_data = "not a dictionary"
    secret_key = "secret"
    with pytest.raises(TypeError):
        task_func(req_data=req_data, secret_key=secret_key)