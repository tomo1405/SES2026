from typing import Counter

from src_0807 import task_func


def test_task_func_with_default_n():
    text = "This is a test text with some common words"
    result = task_func(text)
    assert isinstance(result, Counter)
    assert ('this', 'is') in result
    assert ('is', 'a') in result
    assert ('a', 'test') in result
    assert ('test', 'text') in result
    assert ('text', 'with') in result
    assert ('with', 'some') in result
    assert ('some', 'common') in result
    assert ('common', 'words') in result

def test_task_func_with_custom_n():
    text = "Python is a great programming language"
    n = 3
    result = task_func(text, n)
    assert isinstance(result, Counter)
    assert ('python', 'is', 'a') in result
    assert ('is', 'a', 'great') in result
    assert ('a', 'great', 'programming') in result
    assert ('great', 'programming', 'language') in result

def test_task_func_with_no_words():
    text = "!!!"
    result = task_func(text)
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_task_func_with_single_word():
    text = "Python"
    result = task_func(text)
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_task_func_with_empty_string():
    text = ""
    result = task_func(text)
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_task_func_with_stopwords_only():
    text = "is a the of and"
    result = task_func(text)
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_task_func_with_punctuation():
    text = "Hello, world! This is a test."
    result = task_func(text)
    assert isinstance(result, Counter)
    assert ('hello', 'world') in result
    assert ('world', 'this') in result
    assert ('this', 'is') in result
    assert ('is', 'a') in result
    assert ('a', 'test') in result