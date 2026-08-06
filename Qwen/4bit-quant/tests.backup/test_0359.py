import pytest
from src_0359 import task_func

def test_task_func_valid_json():
    json_list = '{"number_list": [1, 2, 3, 4]}'
    r = 2
    expected_output = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    assert task_func(json_list, r) == expected_output

def test_task_func_invalid_json():
    json_list = '{"number_list": [1, 2, 3, 4]'
    r = 2
    with pytest.raises(json.JSONDecodeError):
        task_func(json_list, r)

def test_task_func_empty_number_list():
    json_list = '{"number_list": []}'
    r = 2
    expected_output = []
    assert task_func(json_list, r) == expected_output

def test_task_func_r_greater_than_list_length():
    json_list = '{"number_list": [1, 2]}'
    r = 3
    expected_output = []
    assert task_func(json_list, r) == expected_output

def test_task_func_r_zero():
    json_list = '{"number_list": [1, 2, 3]}'
    r = 0
    expected_output = [()]
    assert task_func(json_list, r) == expected_output

def test_task_func_r_one():
    json_list = '{"number_list": [1, 2, 3]}'
    r = 1
    expected_output = [(1,), (2,), (3,)]
    assert task_func(json_list, r) == expected_output

def test_task_func_non_list_number_list():
    json_list = '{"number_list": "not a list"}'
    r = 2
    with pytest.raises(TypeError):
        task_func(json_list, r)