import pytest
from src_1099 import task_func

def test_task_func_no_urls():
    text = "Hello world! Visit https://example.com for more info."
    top_n = 2
    expected = [('Hello', 1), ('world', 1)]
    assert task_func(text, top_n) == expected

def test_task_func_with_urls():
    text = "Check out http://test.com and https://another.com for details."
    top_n = 3
    expected = []
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

def test_task_func_multiple_words():
    text = "Python Python is great. I love Python!"
    top_n = 2
    expected = [('Python', 3), ('is', 1)]
    assert task_func(text, top_n) == expected

def test_task_func_top_n_greater_than_unique_words():
    text = "One two three"
    top_n = 5
    expected = [('One', 1), ('two', 1), ('three', 1)]
    assert task_func(text, top_n) == expected

def test_task_func_case_sensitive():
    text = "Test test TEST"
    top_n = 1
    expected = [('Test', 1)]
    assert task_func(text, top_n) == expected

def test_task_func_punctuation():
    text = "Hello, world! Hello world?"
    top_n = 2
    expected = [('Hello', 2), ('world', 2)]
    assert task_func(text, top_n) == expected