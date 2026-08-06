import pytest
from src_0821 import task_func

def test_task_func_valid_input():
    num_words = 5
    word_length = 8
    words = task_func(num_words, word_length)
    assert len(words) == num_words
    assert all(len(word) == word_length for word in words)

def test_task_func_invalid_input():
    num_words = -1
    word_length = 8
    with pytest.raises(ValueError):
        task_func(num_words, word_length)

    num_words = 5
    word_length = -1
    with pytest.raises(ValueError):
        task_func(num_words, word_length)