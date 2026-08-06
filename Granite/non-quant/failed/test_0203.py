import pytest
import re
import json
from collections import Counter

def task_func(json_str, top_n=10):
    pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    data = json.loads(json_str)
    urls = []

    def extract(dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                extract(value)
            elif isinstance(value, str) and re.match(pattern, value):
                urls.append(value)

    extract(data)
    if not urls:
        return {}
    elif len(urls) <= top_n:
        return dict(Counter(urls))

    return dict(Counter(urls).most_common(top_n))

def test_task_func():
    json_str = '{"key1": "value1", "key2": {"key3": "value3", "key4": "https://www.example.com"}, "key5": "https://www.google.com"}'
    expected_output = {'https://www.example.com': 1, 'https://www.google.com': 1}
    assert task_func(json_str, top_n=2) == expected_output

def test_task_func_no_urls():
    json_str = '{"key1": "value1", "key2": {"key3": "value3", "key4": "invalid_url"}, "key5": "https://www.google.com"}'
    expected_output = {}
    assert task_func(json_str, top_n=2) == expected_output

def test_task_func_top_n():
    json_str = '{"key1": "value1", "key2": {"key3": "value3", "key4": "https://www.example.com"}, "key5": "https://www.google.com", "key6": "https://www.github.com", "key7": "https://www.facebook.com"}'
    expected_output = {'https://www.example.com': 1, 'https://www.google.com': 1}
    assert task_func(json_str, top_n=2) == expected_output