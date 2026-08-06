import pytest
from src_1100 import task_func

def test_task_func_no_urls():
    text = "This is a test text with no urls."
    expected_output = [('test', 1), ('text', 1), ('with', 1), ('no', 1), ('urls', 1)]
    assert sorted(task_func(text)) == sorted(expected_output)

def test_task_func_with_urls():
    text = "This is a test text with http://example.com urls."
    expected_output = [('test', 1), ('text', 1), ('with', 1), ('urls', 1)]
    assert sorted(task_func(text)) == sorted(expected_output)

def test_task_func_empty_string():
    text = ""
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_only_stopwords():
    text = "is a the and"
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_mixed_case():
    text = "This is a TEST text with TEST URLs."
    expected_output = [('TEST', 2), ('text', 1), ('with', 1), ('URLs', 1)]
    assert sorted(task_func(text)) == sorted(expected_output)

def test_task_func_special_characters():
    text = "Hello, world! This is a test."
    expected_output = [('Hello', 1), ('world', 1), ('This', 1), ('is', 1), ('a', 1), ('test', 1)]
    assert sorted(task_func(text)) == sorted(expected_output)