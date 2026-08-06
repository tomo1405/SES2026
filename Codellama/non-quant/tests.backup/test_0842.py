import pytest
from src_0842 import task_func

def test_task_func_valid_json():
    json_string = '{"text": "This is a test string"}'
    expected_result = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'string': 1}
    assert task_func(json_string) == expected_result

def test_task_func_invalid_json():
    json_string = '{"text": "This is a test string"'
    expected_result = {}
    assert task_func(json_string) == expected_result

def test_task_func_empty_string():
    json_string = '{"text": ""}'
    expected_result = {}
    assert task_func(json_string) == expected_result

def test_task_func_no_text_key():
    json_string = '{"foo": "bar"}'
    expected_result = {}
    assert task_func(json_string) == expected_result

def test_task_func_text_key_empty_string():
    json_string = '{"text": ""}'
    expected_result = {}
    assert task_func(json_string) == expected_result

def test_task_func_text_key_with_spaces():
    json_string = '{"text": "   "}'
    expected_result = {}
    assert task_func(json_string) == expected_result

def test_task_func_text_key_with_punctuation():
    json_string = '{"text": "This is a test string!"}'
    expected_result = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'string': 1}
    assert task_func(json_string) == expected_result

def test_task_func_text_key_with_non_alphanumeric_chars():
    json_string = '{"text": "This is a test string!@#$%^&*()_+-=[]{}|;:<>?,./"}'
    expected_result = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'string': 1}
    assert task_func(json_string) == expected_result