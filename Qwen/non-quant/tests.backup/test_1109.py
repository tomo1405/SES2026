import pytest
from src_1109 import task_func

def test_task_func_with_valid_urls():
    result = [
        {"url1": "http://example.com", "data": "value1"},
        {"url2": "https://example.com", "data": "value2"},
        {"url3": "http://example.com", "data": "value3"}
    ]
    expected_output = {"value1": 2}
    assert task_func(result) == expected_output

def test_task_func_with_invalid_urls():
    result = [
        {"url1": "ftp://example.com", "data": "value1"},
        {"url2": "invalid-url", "data": "value2"},
        {"url3": "http://example.com", "data": "value3"}
    ]
    expected_output = {"value1": 1}
    assert task_func(result) == expected_output

def test_task_func_with_no_urls():
    result = [
        {"key1": "value1"},
        {"key2": "value2"},
        {"key3": "value3"}
    ]
    expected_output = {}
    assert task_func(result) == expected_output

def test_task_func_with_empty_list():
    result = []
    expected_output = {}
    assert task_func(result) == expected_output

def test_task_func_with_mixed_data_types():
    result = [
        {"url1": "http://example.com", "data": 123},
        {"url2": "https://example.com", "data": 456},
        {"url3": "http://example.com", "data": 123}
    ]
    expected_output = {123: 2}
    assert task_func(result) == expected_output

def test_task_func_with_case_insensitive_urls():
    result = [
        {"url1": "HTTP://example.com", "data": "value1"},
        {"url2": "https://example.com", "data": "value2"},
        {"url3": "http://EXAMPLE.COM", "data": "value3"}
    ]
    expected_output = {"value1": 3}
    assert task_func(result) == expected_output