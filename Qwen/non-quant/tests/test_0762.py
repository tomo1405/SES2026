from typing import Counter

from src_0762 import task_func


def test_task_func_with_no_none_values_and_no_emails():
    input_json = '{"name": "John", "age": 30, "city": "New York"}'
    expected_output = {
        "data": {"name": "John", "age": 30, "city": "New York"},
        "value_counts": Counter({"John": 1, 30: 1, "New York": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_none_values():
    input_json = '{"name": "John", "age": null, "city": "New York"}'
    expected_output = {
        "data": {"name": "John", "city": "New York"},
        "value_counts": Counter({"John": 1, "New York": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_emails():
    input_json = '{"name": "John", "email": "john@example.com", "city": "New York"}'
    expected_output = {
        "data": {"name": "John", "email": "None", "city": "New York"},
        "value_counts": Counter({"John": 1, "None": 1, "New York": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_mixed_values():
    input_json = '{"name": "John", "age": null, "email": "john@example.com", "city": "New York"}'
    expected_output = {
        "data": {"name": "John", "email": "None", "city": "New York"},
        "value_counts": Counter({"John": 1, "None": 1, "New York": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_empty_json():
    input_json = '{}'
    expected_output = {
        "data": {},
        "value_counts": Counter()
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_single_key_value_pair():
    input_json = '{"name": "John"}'
    expected_output = {
        "data": {"name": "John"},
        "value_counts": Counter({"John": 1})
    }
    assert task_func(input_json) == expected_output

def test_task_func_with_non_string_keys():
    input_json = '{"1": "one", "2": "two", "3": null}'
    expected_output = {
        "data": {"1": "one", "2": "two"},
        "value_counts": Counter({"one": 1, "two": 1})
    }
    assert task_func(input_json) == expected_output