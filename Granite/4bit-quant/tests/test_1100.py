import pytest
from src_1100 import task_func

def test_task_func():
    text = "This is a test sentence with some URLs: http://example.com and http://test.com"
    expected_result = [
        ('This', 1),
        ('is', 1),
        ('a', 1),
        ('test', 1),
        ('sentence', 1),
        ('with', 1),
        ('some', 1),
        ('URLs', 1),
        ('and', 1),
        ('http', 1),
        ('example', 1),
        ('com', 1),
        ('test', 1),
        ('com', 1)
    ]
    result = task_func(text)
    assert result == expected_result

def test_task_func_with_stopwords():
    text = "This is a test sentence with some stopwords like 'the' and 'is'"
    expected_result = [
        ('This', 1),
        ('test', 1),
        ('sentence', 1),
        ('with', 1),
        ('some', 1),
        ('stopwords', 1),
        ('like', 1),
        ("'the'", 1),
        ('and', 1),
        ("'is'", 1)
    ]
    result = task_func(text)
    assert result == expected_result

def test_task_func_with_no_text():
    text = ""
    expected_result = []
    result = task_func(text)
    assert result == expected_result