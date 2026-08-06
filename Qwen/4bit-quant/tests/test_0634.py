import pytest
from src_0634 import task_func

def test_task_func_with_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_with_single_word():
    result = task_func("hello")
    assert result == {'hello': 1}

def test_task_func_with_multiple_words():
    result = task_func("hello world hello")
    assert result == {'world': 1}

def test_task_func_with_stopwords():
    result = task_func("this is a test sentence with some stopwords")
    assert result == {'sentence': 1, 'some': 1, 'stopwords': 1, 'test': 1, 'with': 1}

def test_task_func_with_case_insensitivity():
    result = task_func("Hello hello HELLO")
    assert result == {'hello': 3}

def test_task_func_with_punctuation():
    result = task_func("Hello, world! Hello... world?")
    assert result == {'hello': 2, 'world': 2}

def test_task_func_with_duplicate_words():
    result = task_func("repeat repeat repeat word")
    assert result == {'repeat': 3, 'word': 1}

def test_task_func_with_numbers():
    result = task_func("number 123 number")
    assert result == {'number': 2}

def test_task_func_with_special_characters():
    result = task_func("!@# $%^ &*() special")
    assert result == {'special': 1}