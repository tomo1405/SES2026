python
import numpy as np
import random
import pytest

from src_0555 import task_func

def test_task_func():
    MIN_WORDS = 5
    MAX_WORDS = 10
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

    sentence_length = np.random.randint(MIN_WORDS, MAX_WORDS + 1)
    first_half = [random.choice(WORDS_POOL) for _ in range(sentence_length // 2)]

    # For odd-length sentences, add a middle word
    if sentence_length % 2 == 1:
        middle_word = [random.choice(WORDS_POOL)]
        second_half = first_half[::-1]
        sentence = first_half + middle_word + second_half
    else:
        second_half = first_half[::-1]
        sentence = first_half + second_half

    expected_sentence = ' '.join(sentence)

    assert task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL) == expected_sentence