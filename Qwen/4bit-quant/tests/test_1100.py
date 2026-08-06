import pytest
from src_1100 import task_func

def test_task_func_with_no_stopwords():
    text = "This is a test sentence with no stopwords."
    expected_output = [('test', 1), ('sentence', 1), ('no', 1), ('stopwords', 1)]
    assert task_func(text) == expected_output

def test_task_func_with_all_stopwords():
    text = "This is a test sentence with all stopwords."
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_with_mixed_content():
    text = "Hello world! This is a test sentence with mixed content."
    expected_output = [('hello', 1), ('world', 1), ('test', 1), ('sentence', 1), ('mixed', 1), ('content', 1)]
    assert task_func(text) == expected_output

def test_task_func_with_numbers():
    text = "This is a test sentence with numbers 123 and symbols #@$."
    expected_output = [('test', 1), ('sentence', 1), ('numbers', 1), ('and', 1), ('symbols', 1)]
    assert task_func(text) == expected_output

def test_task_func_with_urls():
    text = "Check out this URL http://example.com and see what happens."
    expected_output = [('check', 1), ('out', 1), ('this', 1), ('url', 1), ('and', 1), ('see', 1), ('what', 1), ('happens', 1)]
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_with_single_word():
    text = "word"
    expected_output = [('word', 1)]
    assert task_func(text) == expected_output

def test_task_func_with_repeated_words():
    text = "repeat repeat repeat"
    expected_output = [('repeat', 3)]
    assert task_func(text) == expected_output