import pytest
from src_1099 import task_func

def test_task_func_no_urls():
    text = "Hello world! This is a test."
    top_n = 2
    expected = [('test', 1), ('This', 1)]
    assert task_func(text, top_n) == expected

def test_task_func_with_urls():
    text = "Check out this link http://example.com and see the results!"
    top_n = 3
    expected = [('link', 1), ('this', 1), ('see', 1)]
    assert task_func(text, top_n) == expected

def test_task_func_empty_text():
    text = ""
    top_n = 5
    expected = []
    assert task_func(text, top_n) == expected

def test_task_func_single_word():
    text = "Python"
    top_n = 1
    expected = [('Python', 1)]
    assert task_func(text, top_n) == expected

def test_task_func_punctuation():
    text = "Hello, world! Hello... world?"
    top_n = 2
    expected = [('world', 2), ('Hello', 2)]
    assert task_func(text, top_n) == expected

def test_task_func_case_insensitivity():
    text = "Hello hello HELLO"
    top_n = 1
    expected = [('Hello', 3)]
    assert task_func(text, top_n) == expected

def test_task_func_top_n_greater_than_unique_words():
    text = "A B C"
    top_n = 5
    expected = [('A', 1), ('B', 1), ('C', 1)]
    assert task_func(text, top_n) == expected

def test_task_func_large_text():
    text = " ".join(["word"] * 100 + ["another"] * 50 + ["word"] * 50)
    top_n = 2
    expected = [('word', 150), ('another', 50)]
    assert task_func(text, top_n) == expected