import pytest
from src_0634 import task_func

def test_task_func_no_input():
    assert task_func("") == {}

def test_task_func_single_word():
    assert task_func("hello") == {'hello': 1}

def test_task_func_multiple_words():
    assert task_func("hello world hello") == {'world': 1}

def test_task_func_case_insensitivity():
    assert task_func("Hello hello") == {'hello': 2}

def test_task_func_punctuation():
    assert task_func("Hello, world!") == {'hello': 1, 'world': 1}

def test_task_func_stopwords():
    assert task_func("the quick brown fox jumps over the lazy dog") == {'brown': 1, 'dog': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'over': 1, 'quick': 1}

def test_task_func_duplicates():
    assert task_func("repeat repeat repeat") == {'repeat': 3}

def test_task_func_mixed_case():
    assert task_func("The THE the") == {'the': 3}

def test_task_func_numbers():
    assert task_func("one 1 two 2") == {'1': 1, '2': 1, 'one': 1, 'two': 1}