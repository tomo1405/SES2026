import pytest
from src_0842 import task_func

def test_task_func_valid_json():
    json_string = '{"text": "Hello, world! Hello, everyone."}'
    expected_output = {'hello': 2, 'world': 1, 'everyone': 1}
    assert task_func(json_string) == expected_output

def test_task_func_empty_text():
    json_string = '{"text": ""}'
    expected_output = {}
    assert task_func(json_string) == expected_output

def test_task_func_no_text_key():
    json_string = '{"other_key": "value"}'
    expected_output = {}
    assert task_func(json_string) == expected_output

def test_task_func_invalid_json():
    json_string = '{"text": "Hello, world!"'
    expected_output = {}
    assert task_func(json_string) == expected_output

def test_task_func_punctuation_removal():
    json_string = '{"text": "Hello... world!!!"}'
    expected_output = {'hello': 1, 'world': 1}
    assert task_func(json_string) == expected_output

def test_task_func_case_insensitivity():
    json_string = '{"text": "Hello hello HELLO"}'
    expected_output = {'hello': 3}
    assert task_func(json_string) == expected_output

def test_task_func_non_alphanumeric_removal():
    json_string = '{"text": "Hello, world! 123 @#%"}'
    expected_output = {'hello': 1, 'world': 1, '123': 1}
    assert task_func(json_string) == expected_output