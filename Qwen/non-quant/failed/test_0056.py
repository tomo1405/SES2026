import pytest
from src_0056 import task_func

def test_task_func_no_sentences():
    text = ""
    result = task_func(text)
    assert result.empty

def test_task_func_single_sentence_no_words():
    text = "."
    result = task_func(text)
    assert result.empty

def test_task_func_single_sentence_with_words():
    text = "Hello world."
    result = task_func(text)
    assert result["Sentence 1"] == 2

def test_task_func_multiple_sentences():
    text = "Hello world. This is a test. Ignore these words."
    result = task_func(text)
    assert result["Sentence 1"] == 2
    assert result["Sentence 2"] == 4
    assert result["Sentence 3"] == 0

def test_task_func_with_stopwords():
    text = "Those are the words to ignore. But this one should count."
    result = task_func(text)
    assert result["Sentence 1"] == 0
    assert result["Sentence 2"] == 5

def test_task_func_empty_sentence():
    text = "This is a test. . Another sentence."
    result = task_func(text)
    assert result["Sentence 1"] == 4
    assert result["Sentence 2"] == 0
    assert result["Sentence 3"] == 2

def test_task_func_case_insensitivity():
    text = "HELLO WORLD. tHIs IS a TeSt."
    result = task_func(text)
    assert result["Sentence 1"] == 2
    assert result["Sentence 2"] == 4