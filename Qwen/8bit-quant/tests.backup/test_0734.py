import pytest
from src_0734 import task_func

def test_task_func_with_empty_string():
    assert task_func("") == 0

def test_task_func_with_single_word():
    assert task_func("Hello") == 0

def test_task_func_with_multiple_words():
    assert task_func("Hello world!") == 1

def test_task_func_with_punctuation():
    assert task_func("Hello, world!") == 1

def test_task_func_with_stopwords_only():
    assert task_func("I am a test.") == 0

def test_task_func_with_non_stopwords():
    assert task_func("This is a simple test.") == 2

def test_task_func_with_mixed_content():
    assert task_func("Hello, this is a test!") == 3

def test_task_func_with_large_input():
    large_input = " ".join(["word"] * 1000)
    assert task_func(large_input) == 999

def test_task_func_with_special_characters():
    assert task_func("!@#$%^&*()") == 0

def test_task_func_with_numbers():
    assert task_func("12345 67890") == 0

def test_task_func_with_mixed_case():
    assert task_func("Hello WORLD!") == 1