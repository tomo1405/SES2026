import pytest
from src_0821 import task_func
import random
import string

# Constants
LETTERS = string.ascii_letters

def test_task_func():
    num_words = 5
    word_length = 10
    words = task_func(num_words, word_length)
    assert len(words) == num_words
    for word in words:
        assert len(word) == word_length
        for char in word:
            assert char in LETTERS
    with pytest.raises(ValueError):
        task_func(-1, word_length)
    with pytest.raises(ValueError):
        task_func(num_words, -1)