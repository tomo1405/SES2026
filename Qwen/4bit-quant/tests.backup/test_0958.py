import pytest
from src_0958 import task_func

def test_task_func_empty_string():
    assert task_func("") == (0, 0, 0)

def test_task_func_single_word_no_punctuation():
    assert task_func("hello") == (1, 5, 5)

def test_task_func_single_word_with_punctuation():
    assert task_func("hello!") == (1, 5, 5)

def test_task_func_multiple_words_no_punctuation():
    assert task_func("hello world") == (2, 10, 7)

def test_task_func_multiple_words_with_punctuation():
    assert task_func("hello, world!") == (2, 10, 7)

def test_task_func_whitespace_only():
    assert task_func("   ") == (0, 0, 0)

def test_task_func_special_characters():
    assert task_func("!@#$%^&*()") == (0, 0, 0)

def test_task_func_mixed_case():
    assert task_func("Hello, World!") == (2, 10, 7)

def test_task_func_numbers():
    assert task_func("123 456") == (2, 6, 3)

def test_task_func_numbers_with_punctuation():
    assert task_func("123! 456?") == (2, 6, 3)