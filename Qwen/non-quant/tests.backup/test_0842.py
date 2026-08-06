import pytest
from src_0842 import task_func

def test_task_func_valid_json():
    json_input = '{"text": "Hello, world! Hello again."}'
    expected_output = {'hello': 2, 'world': 1, 'again': 1}
    assert task_func(json_input) == expected_output

def test_task_func_no_text_key():
    json_input = '{"no_text": "Hello, world!"}'
    expected_output = {}
    assert task_func(json_input) == expected_output

def test_task_func_empty_text():
    json_input = '{"text": ""}'
    expected_output = {}
    assert task_func(json_input) == expected_output

def test_task_func_non_alphanumeric_characters():
    json_input = '{"text": "Hello, world! 123 @#%&*()"}'
    expected_output = {'hello': 1, 'world': 1, '123': 1}
    assert task_func(json_input) == expected_output

def test_task_func_invalid_json():
    json_input = '{"text": "Hello, world!"'
    expected_output = {}
    assert task_func(json_input) == expected_output

def test_task_func_punctuation_removal():
    json_input = '{"text": "Hello... world!!!"}'
    expected_output = {'hello': 1, 'world': 1}
    assert task_func(json_input) == expected_output

def test_task_func_case_insensitivity():
    json_input = '{"text": "Hello hello HELLO"}'
    expected_output = {'hello': 3}
    assert task_func(json_input) == expected_output