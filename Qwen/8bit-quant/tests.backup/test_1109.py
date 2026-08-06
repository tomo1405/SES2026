import pytest
from src_1109 import task_func

def test_task_func_with_valid_urls():
    input_data = [
        {"url1": "http://example.com", "data": "info1"},
        {"url2": "https://example.com", "data": "info2"},
        {"url3": "ftp://example.com", "data": "info3"},
        {"url4": "http://example.com", "data": "info4"}
    ]
    expected_output = {"info1": 2}
    assert task_func(input_data) == expected_output

def test_task_func_with_no_urls():
    input_data = [
        {"key1": "value1", "data": "info1"},
        {"key2": "value2", "data": "info2"}
    ]
    expected_output = {}
    assert task_func(input_data) == expected_output

def test_task_func_with_mixed_data():
    input_data = [
        {"url1": "http://example.com", "data": "info1"},
        {"key2": "value2", "data": "info2"},
        {"url3": "ftp://example.com", "data": "info3"},
        {"url4": "http://example.com", "data": "info1"}
    ]
    expected_output = {"info1": 2}
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_list():
    input_data = []
    expected_output = {}
    assert task_func(input_data) == expected_output

def test_task_func_with_invalid_urls():
    input_data = [
        {"invalid_url": "not_a_url", "data": "info1"},
        {"another_invalid_url": "still_not_a_url", "data": "info2"}
    ]
    expected_output = {}
    assert task_func(input_data) == expected_output

def test_task_func_with_single_url():
    input_data = [
        {"url1": "http://example.com", "data": "info1"}
    ]
    expected_output = {"info1": 1}
    assert task_func(input_data) == expected_output