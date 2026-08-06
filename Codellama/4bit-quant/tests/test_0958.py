import pytest
from src_0958 import task_func

def test_task_func():
    text = "Hello, World!"
    expected_words = 2
    expected_chars = 13
    expected_unique_chars = 12

    words, chars, unique_chars = task_func(text)

    assert words == expected_words
    assert chars == expected_chars
    assert unique_chars == expected_unique_chars

def test_task_func_empty_string():
    text = ""
    expected_words = 0
    expected_chars = 0
    expected_unique_chars = 0

    words, chars, unique_chars = task_func(text)

    assert words == expected_words
    assert chars == expected_chars
    assert unique_chars == expected_unique_chars

def test_task_func_punctuation():
    text = "Hello, World! How are you?"
    expected_words = 4
    expected_chars = 19
    expected_unique_chars = 18

    words, chars, unique_chars = task_func(text)

    assert words == expected_words
    assert chars == expected_chars
    assert unique_chars == expected_unique_chars

def test_task_func_unicode():
    text = "Hello, World! 你好"
    expected_words = 2
    expected_chars = 15
    expected_unique_chars = 14

    words, chars, unique_chars = task_func(text)

    assert words == expected_words
    assert chars == expected_chars
    assert unique_chars == expected_unique_chars