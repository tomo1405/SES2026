import pytest
from src_0555 import task_func

def test_task_func():
    # Test with even-length sentences
    sentence_length = 4
    words_pool = ['apple', 'banana', 'orange']
    expected_sentence = 'apple banana orange banana apple'
    assert task_func(2, sentence_length, words_pool) == expected_sentence

    # Test with odd-length sentences
    sentence_length = 5
    words_pool = ['apple', 'banana', 'orange']
    expected_sentence = 'apple banana orange apple banana'
    assert task_func(2, sentence_length, words_pool) == expected_sentence

    # Test with different word pools
    sentence_length = 4
    words_pool = ['cat', 'dog', 'mouse']
    expected_sentence = 'cat dog mouse dog cat'
    assert task_func(2, sentence_length, words_pool) == expected_sentence