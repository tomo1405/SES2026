import pytest
from src_0958 import task_func

def test_task_func():
    text = "Hello, World!"
    expected_words = 2
    expected_chars = 12
    expected_unique_chars = 10

    words, chars, unique_chars = task_func(text)

    assert words == expected_words
    assert chars == expected_chars
    assert unique_chars == expected_unique_chars