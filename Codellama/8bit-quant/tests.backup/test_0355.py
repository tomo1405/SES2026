import pytest
from src_0355 import task_func

def test_task_func():
    sentences_dict = {'sentence1': 'the quick brown fox jumps over the lazy dog',
                     'sentence2': 'the quick brown fox jumps over the lazy dog',
                     'sentence3': 'the quick brown fox jumps over the lazy dog'}
    word_keys = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
    expected_frequencies = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    word_counts = task_func(sentences_dict, word_keys)

    assert len(word_counts) == len(word_keys)
    assert all(word_counts[word] == expected_frequencies[i] for i, word in enumerate(word_keys))