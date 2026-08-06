import pytest
from src_1123 import task_func

def test_task_func_no_urls():
    result = task_func("This is a test string without any URLs.")
    assert result == {}

def test_task_func_single_url():
    result = task_func("Check out this website: http://example.com")
    assert "example.com" in result
    assert isinstance(result["example.com"], str) or result["example.com"] is None

def test_task_func_multiple_urls():
    result = task_func("Visit http://example.com and https://another-example.org for more info.")
    assert "example.com" in result
    assert "another-example.org" in result
    assert isinstance(result["example.com"], str) or result["example.com"] is None
    assert isinstance(result["another-example.org"], str) or result["another-example.org"] is None

def test_task_func_invalid_url():
    result = task_func("This URL is invalid: http://invalid-url-xyz123")
    assert "invalid-url-xyz123" in result
    assert result["invalid-url-xyz123"] is None

def test_task_func_mixed_content():
    result = task_func("Here's a mix: text, http://example.com, and more text.")
    assert "example.com" in result
    assert isinstance(result["example.com"], str) or result["example.com"] is None

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_only_commas():
    result = task_func(",,,,")
    assert result == {}