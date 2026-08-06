import pytest
import itertools
import json
from src_0359 import task_func

def test_task_func():
    json_list = '{"number_list": [1, 2, 3, 4, 5]}'
    r = 3
    expected_output = [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
    actual_output = task_func(json_list, r)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_json():
    json_list = '{"number_list": [1, 2, 3, 4, 5'
    r = 3
    with pytest.raises(Exception) as exc_info:
        task_func(json_list, r)
    assert "JSON decode error" in str(exc_info.value), "Expected JSON decode error, but got a different exception"

def test_task_func_with_invalid_r():
    json_list = '{"number_list": [1, 2, 3, 4, 5]}'
    r = -1
    with pytest.raises(Exception) as exc_info:
        task_func(json_list, r)
    assert "Invalid value for r" in str(exc_info.value), "Expected 'Invalid value for r', but got a different exception"