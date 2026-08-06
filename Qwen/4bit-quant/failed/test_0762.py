import pytest
from src_0762 import task_func

def test_task_func_no_none_values():
    input_json = '{"name": "John", "age": 30}'
    expected_output = {
        "data": {"name": "John", "age": 30},
        "value_counts": Counter({"John": 1, 30: 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_none_values():
    input_json = '{"name": "John", "age": null, "email": "john@example.com"}'
    expected_output = {
        "data": {"name": "John"},
        "value_counts": Counter({"John": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_email_replacement():
    input_json = '{"name": "John", "email": "john@example.com"}'
    expected_output = {
        "data": {"name": "John", "email": "None"},
        "value_counts": Counter({"John": 1, "None": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_multiple_emails():
    input_json = '{"name": "John", "email": "john@example.com", "secondary_email": "jane@example.com"}'
    expected_output = {
        "data": {"name": "John", "email": "None", "secondary_email": "None"},
        "value_counts": Counter({"John": 1, "None": 2})
    }
    assert task_func(input_json) == expected_output

def test_task_func_empty_json():
    input_json = '{}'
    expected_output = {
        "data": {},
        "value_counts": Counter()
    }
    assert task_func(input_json) == expected_output

def test_task_func_non_string_values():
    input_json = '{"name": "John", "age": 30, "is_student": false}'
    expected_output = {
        "data": {"name": "John", "age": 30, "is_student": False},
        "value_counts": Counter({"John": 1, 30: 1, False: 1})
    }
    assert task_func(input_json) == expected_output