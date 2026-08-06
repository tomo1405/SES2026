import string
import re
from src_0958 import task_func
import pytest

def test_task_func():
    text = "Hello, world!"
    word_count, char_count, unique_chars = task_func(text)
    assert word_count == 2
    assert char_count == 10
    assert unique_chars == 7

def test_task_func_with_punctuation():
    text = "Hello, world! How are you?"
    word_count, char_count, unique_chars = task_func(text)
    assert word_count == 4
    assert char_count == 16
    assert unique_chars == 9

def test_task_func_with_spaces():
    text = "   Hello   world!  "
    word_count, char_count, unique_chars = task_func(text)
    assert word_count == 2
    assert char_count == 10
    assert unique_chars == 7

def test_task_func_with_empty_string():
    text = ""
    word_count, char_count, unique_chars = task_func(text)
    assert word_count == 0
    assert char_count == 0
    assert unique_chars == 0

def test_task_func_with_only_punctuation():
    text = ".,!?"
    word_count, char_count, unique_chars = task_func(text)
    assert word_count == 0
    assert char_count == 0
    assert unique_chars == 0