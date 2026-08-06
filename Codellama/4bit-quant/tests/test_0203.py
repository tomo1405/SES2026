import pytest
from src_0203 import task_func

def test_task_func():
    json_str = '{"key1": "value1", "key2": "value2", "key3": "value3"}'
    top_n = 2
    expected_result = {'value1': 1, 'value2': 1}
    assert task_func(json_str, top_n) == expected_result

def test_task_func_with_empty_json():
    json_str = ''
    top_n = 2
    expected_result = {}
    assert task_func(json_str, top_n) == expected_result

def test_task_func_with_invalid_json():
    json_str = '{"key1": "value1", "key2": "value2", "key3": "value3"'
    top_n = 2
    expected_result = {}
    assert task_func(json_str, top_n) == expected_result

def test_task_func_with_top_n_greater_than_urls():
    json_str = '{"key1": "value1", "key2": "value2", "key3": "value3"}'
    top_n = 4
    expected_result = {'value1': 1, 'value2': 1, 'value3': 1}
    assert task_func(json_str, top_n) == expected_result

def test_task_func_with_top_n_less_than_urls():
    json_str = '{"key1": "value1", "key2": "value2", "key3": "value3"}'
    top_n = 2
    expected_result = {'value1': 1, 'value2': 1}
    assert task_func(json_str, top_n) == expected_result