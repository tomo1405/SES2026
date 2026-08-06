import pytest
from src_1109 import task_func

def test_task_func_with_valid_urls():
    result = [
        {"url1": "https://example.com", "url2": "http://example.org"},
        {"url3": "ftp://example.net", "url4": "https://example.com"}
    ]
    expected_output = {"https://example.com": 2}
    assert task_func(result) == expected_output

def test_task_func_with_no_valid_urls():
    result = [
        {"invalid_url": "not-a-url", "another_invalid": "still-not-a-url"},
        {"yet_another_invalid": "definitely-not-a-url"}
    ]
    expected_output = {}
    assert task_func(result) == expected_output

def test_task_func_with_mixed_valid_and_invalid_urls():
    result = [
        {"valid_url": "https://example.com", "invalid_url": "not-a-url"},
        {"another_valid_url": "https://example.com", "another_invalid": "still-not-a-url"}
    ]
    expected_output = {"https://example.com": 2}
    assert task_func(result) == expected_output

def test_task_func_with_empty_list():
    result = []
    expected_output = {}
    assert task_func(result) == expected_output

def test_task_func_with_empty_dicts():
    result = [{}, {}]
    expected_output = {}
    assert task_func(result) == expected_output

def test_task_func_with_single_url():
    result = [{"single_url": "https://example.com"}]
    expected_output = {"https://example.com": 1}
    assert task_func(result) == expected_output

def test_task_func_with_multiple_same_urls():
    result = [
        {"same_url": "https://example.com"},
        {"same_url": "https://example.com"},
        {"same_url": "https://example.com"}
    ]
    expected_output = {"https://example.com": 3}
    assert task_func(result) == expected_output