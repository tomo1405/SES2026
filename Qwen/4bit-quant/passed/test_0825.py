import pytest
from src_0825 import task_func

def test_task_func_no_text():
    assert task_func("") == (0, 0)

def test_task_func_no_words_only_punctuation():
    assert task_func("!!!@@@###") == (0, 9)

def test_task_func_no_punctuation_only_words():
    assert task_func("hello world") == (2, 0)

def test_task_func_with_words_and_punctuation():
    assert task_func("Hello, world!") == (2, 2)

def test_task_func_with_numbers():
    assert task_func("123 456") == (2, 0)

def test_task_func_with_special_characters():
    assert task_func("$$$hello!!!world@@@") == (2, 9)

def test_task_func_with_mixed_content():
    assert task_func("This is a test, with: some; punctuation!") == (7, 5)