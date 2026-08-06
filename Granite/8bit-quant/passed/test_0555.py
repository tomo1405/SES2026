import pytest
from src_0555 import task_func

def test_task_func():
    MIN_WORDS = 1
    MAX_WORDS = 10
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)

    assert isinstance(sentence, str)
    assert len(sentence.split()) >= MIN_WORDS and len(sentence.split()) <= MAX_WORDS
    for word in sentence.split():
        assert word in WORDS_POOL