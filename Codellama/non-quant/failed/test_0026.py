import pytest
from src_0026 import task_func

def test_task_func():
    data_dict = {"key1": "value1", "key2": "value2"}
    expected_result = "eJyb0b0KwkAMhf/Bw02YQJg=="
    assert task_func(data_dict) == expected_result

def test_task_func_with_empty_dict():
    data_dict = {}
    expected_result = "eJwBwQEAACAIAQ/Bw02YQJg=="
    assert task_func(data_dict) == expected_result

def test_task_func_with_invalid_input():
    data_dict = "invalid input"
    with pytest.raises(TypeError):
        task_func(data_dict)