import pytest
from src_1099 import task_func

def test_task_func_no_urls():
    text = "This is a test text with no urls"
    top_n = 2
    expected_output = [('test', 1), ('text', 1)]
    assert task_func(text, top_n) == expected_output

def test_task_func_with_urls():
    text = "This is a test text with a url http://example.com"
    top_n = 2
    expected_output = [('test', 1), ('text', 1)]
    assert task_func(text, top_n) == expected_output

def test_task_func_empty_text():
    text = ""
    top_n = 3
    expected_output = []
    assert task_func(text, top_n) == expected_output

def test_task_func_top_n_greater_than_unique_words():
    text = "This is a test"
    top_n = 5
    expected_output = [('This', 1), ('is', 1), ('a', 1), ('test', 1)]
    assert task_func(text, top_n) == expected_output

def test_task_func_case_insensitivity():
    text = "This is a test. This TEST is a TEST."
    top_n = 2
    expected_output = [('test', 2), ('this', 2)]
    assert task_func(text, top_n) == expected_output

def test_task_func_punctuation():
    text = "Hello, world! Hello world?"
    top_n = 2
    expected_output = [('hello', 2), ('world', 2)]
    assert task_func(text, top_n) == expected_output

def test_task_func_numbers():
    text = "Number 123 and number 456"
    top_n = 2
    expected_output = [('number', 2)]
    assert task_func(text, top_n) == expected_output

def test_task_func_special_characters():
    text = "Special characters @#$%^&*() should not affect"
    top_n = 2
    expected_output = [('special', 1), ('characters', 1)]
    assert task_func(text, top_n) == expected_output