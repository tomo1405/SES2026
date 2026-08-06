import pytest
from src_0842 import task_func

def test_task_func_valid_json():
    json_input = '{"text": "Hello, world! Hello, everyone."}'
    expected_output = {'hello': 2, 'world': 1, 'everyone': 1}
    assert task_func(json_input) == expected_output

def test_task_func_empty_text():
    json_input = '{"text": ""}'
    expected_output = {}
    assert task_func(json_input) == expected_output

def test_task_func_no_text_key():
    json_input = '{"other_key": "value"}'
    expected_output = {}
    assert task_func(json_input) == expected_output

def test_task_func_invalid_json():
    json_input = '{"text": "Hello, world!"'  # Missing closing brace
    expected_output = {}
    assert task_func(json_input) == expected_output

def test_task_func_special_characters():
    json_input = '{"text": "Hello, @world! #Python & coding."}'
    expected_output = {'hello': 1, 'world': 1, 'python': 1, 'coding': 1}
    assert task_func(json_input) == expected_output

def test_task_func_mixed_case():
    json_input = '{"text": "Hello, World! hello, WORLD."}'
    expected_output = {'hello': 3, 'world': 2}
    assert task_func(json_input) == expected_output

def test_task_func_numbers():
    json_input = '{"text": "Hello, world! 123 123."}'
    expected_output = {'hello': 1, 'world': 1, '123': 2}
    assert task_func(json_input) == expected_output