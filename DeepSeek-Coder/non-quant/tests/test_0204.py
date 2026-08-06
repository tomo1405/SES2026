import pytest
from src_0204 import task_func

def test_task_func_empty_input():
    assert task_func(input_data='') == []

def test_task_func_valid_input():
    input_data = '{"recipient": "recipient@example.com", "names": ["Alice", "Bob"]}'
    assert task_func(input_data=input_data) == ["Alice", "Bob"]

def test_task_func_invalid_input():
    input_data = 'invalid_json'
    assert task_func(input_data=input_data) == []

def test_task_func_no_names():
    input_data = '{"recipient": "recipient@example.com"}'
    assert task_func(input_data=input_data) == []

def test_task_func_with_smtp():
    input_data = '{"recipient": "recipient@example.com", "names": ["Alice", "Bob"]}'
    assert task_func(input_data=input_data) == ["Alice", "Bob"]