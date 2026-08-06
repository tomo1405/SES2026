import pytest
from src_1100 import task_func

def test_task_func():
    text = "This is a sample text with some URLs: http://example.com and https://www.google.com"
    expected_result = [
        ('text', 1),
        ('sample', 1),
        ('some', 1),
        ('urls', 1),
        ('example', 1),
        ('google', 1)
    ]
    assert task_func(text) == expected_result

def test_task_func_with_stopwords():
    text = "This is a sample text with some common words like 'the' and 'is'"
    expected_result = [
        ('text', 1),
        ('sample', 1),
        ('some', 1),
        ('common', 1),
        ('words', 1),
        ('like', 1)
    ]
    assert task_func(text) == expected_result

def test_task_func_with_empty_text():
    text = ""
    expected_result = []
    assert task_func(text) == expected_result

def test_task_func_with_no_urls():
    text = "This is a sample text without any URLs"
    expected_result = [
        ('text', 1),
        ('sample', 1),
        ('without', 1),
        ('any', 1),
        ('urls', 1)
    ]
    assert task_func(text) == expected_result