import pytest
from src_0825 import task_func

def test_task_func():
    text = "Hello, world!"
    expected_words = 2
    expected_punctuation_marks = 2

    words, punctuation_marks = task_func(text)

    assert words == expected_words
    assert punctuation_marks == expected_punctuation_marks