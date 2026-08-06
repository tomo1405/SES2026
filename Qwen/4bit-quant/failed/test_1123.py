import pytest
from src_1123 import task_func

def test_task_func_no_urls():
    result = task_func("This is a test string without any URLs.")
    assert result == {}

def test_task_func_single_http_url():
    result = task_func("Check out this website: http://example.com")
    assert result == {'example.com': '93.184.216.34'}

def test_task_func_single_https_url():
    result = task_func("Visit our secure site: https://secure.example.com")
    assert result == {'secure.example.com': '93.184.216.34'}

def test_task_func_multiple_urls():
    result = task_func("Here are some URLs: http://example.com and https://secure.example.com")
    assert result == {'example.com': '93.184.216.34', 'secure.example.com': '93.184.216.34'}

def test_task_func_unresolvable_domain():
    result = task_func("This domain should not resolve: http://nonexistentdomain123.com")
    assert result == {'nonexistentdomain123.com': None}

def test_task_func_mixed_urls_and_text():
    result = task_func("Some text with http://example.com and more text with https://secure.example.com and some more text.")
    assert result == {'example.com': '93.184.216.34', 'secure.example.com': '93.184.216.34'}

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}