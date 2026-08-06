import pytest
from src_0203 import task_func

def test_task_func_no_urls():
    json_str = '{"name": "John", "age": 30}'
    result = task_func(json_str)
    assert result == {}

def test_task_func_single_url():
    json_str = '{"name": "John", "website": "http://example.com"}'
    result = task_func(json_str)
    assert result == {'http://example.com': 1}

def test_task_func_multiple_urls():
    json_str = '{"name": "John", "websites": ["http://example.com", "http://test.com", "http://example.com"]}'
    result = task_func(json_str)
    assert result == {'http://example.com': 2, 'http://test.com': 1}

def test_task_func_top_n():
    json_str = '{"websites": ["http://a.com", "http://b.com", "http://a.com", "http://c.com", "http://b.com", "http://d.com"]}'
    result = task_func(json_str, top_n=3)
    assert result == {'http://a.com': 2, 'http://b.com': 2, 'http://c.com': 1}

def test_task_func_nested_urls():
    json_str = '{"user": {"name": "John", "profile": {"website": "http://example.com"}}}'
    result = task_func(json_str)
    assert result == {'http://example.com': 1}

def test_task_func_invalid_json():
    json_str = '{"name": "John", "age": 30'
    with pytest.raises(json.JSONDecodeError):
        task_func(json_str)

def test_task_func_non_string_values():
    json_str = '{"name": "John", "age": 30, "numbers": [1, 2, 3]}'
    result = task_func(json_str)
    assert result == {}

def test_task_func_empty_json():
    json_str = '{}'
    result = task_func(json_str)
    assert result == {}