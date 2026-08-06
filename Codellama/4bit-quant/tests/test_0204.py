import pytest
from src_0204 import task_func

def test_task_func_with_valid_input():
    input_data = '{"recipient": "recipient@example.com", "names": ["Alice", "Bob"]}'
    expected_names = ["Alice", "Bob"]
    assert task_func(input_data) == expected_names

def test_task_func_with_invalid_input():
    input_data = '{"recipient": "recipient@example.com", "names": ["Alice", "Bob"]}'
    expected_names = []
    assert task_func(input_data) == expected_names

def test_task_func_with_missing_recipient():
    input_data = '{"names": ["Alice", "Bob"]}'
    expected_names = []
    assert task_func(input_data) == expected_names

def test_task_func_with_missing_names():
    input_data = '{"recipient": "recipient@example.com"}'
    expected_names = []
    assert task_func(input_data) == expected_names

def test_task_func_with_invalid_json():
    input_data = '{"recipient": "recipient@example.com", "names": ["Alice", "Bob"]}'
    expected_names = []
    assert task_func(input_data) == expected_names