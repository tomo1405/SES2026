import pytest
from src_1100 import task_func

def test_task_func_empty_string():
    assert task_func("") == []

def test_task_func_no_words():
    assert task_func("...") == []

def test_task_func_single_word_not_stopword():
    assert task_func("hello") == [('hello', 1)]

def test_task_func_single_word_stopword():
    assert task_func("the") == []

def test_task_func_multiple_words_with_stopwords():
    text = "this is a test with some stopwords"
    expected = [('test', 1), ('some', 1), ('stopwords', 1)]
    assert sorted(task_func(text)) == sorted(expected)

def test_task_func_with_urls():
    text = "Check out this link http://example.com and see what happens"
    expected = [('Check', 1), ('link', 1), ('see', 1), ('what', 1), ('happens', 1)]
    assert sorted(task_func(text)) == sorted(expected)

def test_task_func_case_insensitivity():
    text = "This is a TEST with SOME STOPWORDS"
    expected = [('TEST', 1), ('SOME', 1), ('STOPWORDS', 1)]
    assert sorted(task_func(text)) == sorted(expected)

def test_task_func_punctuation():
    text = "Hello, world! This is a test."
    expected = [('Hello', 1), ('world', 1), ('This', 1), ('test', 1)]
    assert sorted(task_func(text)) == sorted(expected)

def test_task_func_numbers():
    text = "The year is 2023 and the time is 14:00"
    expected = [('year', 1), ('2023', 1), ('time', 1), ('1400', 1)]
    assert sorted(task_func(text)) == sorted(expected)