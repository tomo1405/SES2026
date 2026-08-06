import pytest
from src_0203 import task_func

def test_task_func_basic():
    json_str = '{"key1": "http://example.com", "key2": "https://www.example.com", "key3": "invalidurl"}'
    result = task_func(json_str=json_str)
    assert result == {'http://example.com': 1, 'https://www.example.com': 1}

def test_task_func_top_n():
    json_str = '{"key1": "http://example.com", "key2": "https://www.example.com", "key3": "invalidurl"}'
    result = task_func(json_str=json_str, top_n=1)
    assert result == {'http://example.com': 1}

def test_task_func_empty():
    json_str = '{"key1": "invalidurl"}'
    result = task_func(json_str=json_str)
    assert result == {}

def test_task_func_no_urls():
    json_str = '{"key1": "invalidurl"}'
    result = task_func(json_str=json_str)
    assert result == {}

def test_task_func_large_input():
    json_str = '{"key1": "http://example.com", "key2": "https://www.example.com", "key3": "http://example.com"}'
    result = task_func(json_str=json_str, top_n=2)
    assert result == {'http://example.com': 2}