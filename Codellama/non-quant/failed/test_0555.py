import pytest
from src_0555 import task_func

def test_task_func():
    # Test with even-length sentences
    MIN_WORDS = 2
    MAX_WORDS = 4
    WORDS_POOL = ['apple', 'banana', 'orange', 'pear']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert len(sentence.split()) == MAX_WORDS
    assert all(word in sentence for word in WORDS_POOL)

    # Test with odd-length sentences
    MIN_WORDS = 3
    MAX_WORDS = 5
    WORDS_POOL = ['apple', 'banana', 'orange', 'pear']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert len(sentence.split()) == MAX_WORDS
    assert all(word in sentence for word in WORDS_POOL)

    # Test with different word pools
    MIN_WORDS = 2
    MAX_WORDS = 4
    WORDS_POOL = ['cat', 'dog', 'mouse', 'elephant']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert len(sentence.split()) == MAX_WORDS
    assert all(word in sentence for word in WORDS_POOL)