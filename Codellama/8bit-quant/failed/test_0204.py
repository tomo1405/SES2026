import pytest
from src_0204 import task_func

def test_task_func_with_valid_input():
    input_data = '{"recipient": "recipient@example.com", "names": ["John", "Jane"]}'
    expected_names = ["John", "Jane"]
    assert task_func(input_data) == expected_names

def test_task_func_with_invalid_input():
    input_data = '{"recipient": "recipient@example.com", "names": ["John", "Jane"]}'
    expected_names = []
    assert task_func(input_data) == expected_names

def test_task_func_with_missing_recipient():
    input_data = '{"names": ["John", "Jane"]}'
    expected_names = []
    assert task_func(input_data) == expected_names

def test_task_func_with_missing_names():
    input_data = '{"recipient": "recipient@example.com"}'
    expected_names = []
    assert task_func(input_data) == expected_names

def test_task_func_with_invalid_json():
    input_data = '{"recipient": "recipient@example.com", "names": ["John", "Jane"]}'
    expected_names = []
    assert task_func(input_data) == expected_names