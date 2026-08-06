import pytest
from src_1100 import task_func

def test_task_func():
    text = "This is a sample text with some URLs: http://example.com and http://test.com"
    expected_result = [
        ('sample', 1),
        ('text', 1),
        ('some', 1),
        ('with', 1),
        (' URLs', 1),
        ('example', 1),
        ('com', 2),
        ('test', 1)
    ]
    result = task_func(text)
    assert result == expected_result

def test_task_func_with_stopwords():
    text = "This is a sample text with some common words like 'the' and 'is'"
    expected_result = [
        ('sample', 1),
        ('text', 1),
        ('some', 1),
        ('common', 1),
        ('words', 1),
        ('like', 1),
        ("'the'", 1),
        ("'is'", 1)
    ]
    result = task_func(text)
    assert result == expected_result

def test_task_func_with_no_text():
    text = ""
    expected_result = []
    result = task_func(text)
    assert result == expected_result