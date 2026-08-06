import pytest
from src_0734 import task_func

def test_task_func_empty_string():
    assert task_func("") == 0

def test_task_func_single_word():
    assert task_func("Hello") == 0

def test_task_func_single_non_stopword():
    assert task_func("Python") == 1

def test_task_func_multiple_words_with_stopwords():
    assert task_func("This is a test") == 1

def test_task_func_multiple_words_no_stopwords():
    assert task_func("Python programming is fun") == 3

def test_task_func_punctuation():
    assert task_func("Hello, world!") == 1

def test_task_func_trailing_space():
    assert task_func("Hello world ") == 1

def test_task_func_only_stopwords():
    assert task_func("is this a test") == 0

def test_task_func_mixed_case():
    assert task_func("HELLO WORLD") == 2

def test_task_func_special_characters():
    assert task_func("$$$Python$$$") == 1

def test_task_func_large_input():
    long_text = " ".join(["word"] * 1000)
    assert task_func(long_text) == 999