import pytest
from src_0821 import task_func
import random
import string

LETTERS = string.ascii_letters

def test_task_func():
    num_words = 5
    word_length = 10
    random.seed(42)
    expected_words = [''.join(random.choice(LETTERS) for _ in range(word_length)) for _ in range(num_words)]
    actual_words = task_func(num_words, word_length)
    assert actual_words == expected_words

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(-1, 10)
    with pytest.raises(ValueError):
        task_func(10, -1)