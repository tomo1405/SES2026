import pytest
from src_0762 import task_func

def test_task_func_none_values_removed():
    input_json = '{"name": null, "age": 30, "email": "test@example.com"}'
    expected_output = {
        "data": {"age": 30, "email": "None"},
        "value_counts": Counter({30: 1, "None": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_emails_replaced():
    input_json = '{"name": "John Doe", "age": 30, "email": "test@example.com"}'
    expected_output = {
        "data": {"name": "John Doe", "age": 30, "email": "None"},
        "value_counts": Counter({"John Doe": 1, 30: 1, "None": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_no_none_or_emails():
    input_json = '{"name": "John Doe", "age": 30}'
    expected_output = {
        "data": {"name": "John Doe", "age": 30},
        "value_counts": Counter({"John Doe": 1, 30: 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_empty_json():
    input_json = '{}'
    expected_output = {"data": {}, "value_counts": Counter()}
    assert task_func(input_json) == expected_output

def test_task_func_all_none_values():
    input_json = '{"name": null, "age": null, "email": null}'
    expected_output = {"data": {}, "value_counts": Counter()}
    assert task_func(input_json) == expected_output