import pytest
from src_0203 import task_func
import json

def test_task_func_no_urls():
    json_str = '{"name": "John", "age": 30}'
    result = task_func(json_str)
    assert result == {}

def test_task_func_single_url():
    json_str = '{"website": "http://example.com"}'
    result = task_func(json_str)
    assert result == {"http://example.com": 1}

def test_task_func_multiple_urls():
    json_str = '{"websites": ["http://example.com", "https://test.com", "http://example.com"]}'
    result = task_func(json_str)
    assert result == {"http://example.com": 2, "https://test.com": 1}

def test_task_func_top_n():
    json_str = '{"websites": ["http://example.com", "https://test.com", "http://example.com", "https://another.com", "https://test.com"]}'
    result = task_func(json_str, top_n=2)
    assert result == {"http://example.com": 2, "https://test.com": 2}

def test_task_func_nested_urls():
    json_str = '{"profile": {"website": "http://example.com"}, "contact": {"social": {"linkedin": "https://linkedin.com"}}}'
    result = task_func(json_str)
    assert result == {"http://example.com": 1, "https://linkedin.com": 1}

def test_task_func_non_url_strings():
    json_str = '{"text": "This is a test string with no URLs"}'
    result = task_func(json_str)
    assert result == {}

def test_task_func_empty_json():
    json_str = '{}'
    result = task_func(json_str)
    assert result == {}

def test_task_func_invalid_json():
    json_str = '{"invalid": "json"'
    with pytest.raises(json.JSONDecodeError):
        task_func(json_str)