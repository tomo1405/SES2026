import pytest
from src_0935 import task_func
from collections import Counter
import hashlib

def test_task_func():
    # Test with a simple word
    word = "hello"
    expected_pairs = ['he', 'el', 'll', 'lo']
    pairs_count = dict(Counter(expected_pairs))
    expected_hash = hashlib.md5(str(pairs_count).encode()).hexdigest()
    assert task_func(word) == expected_hash

    # Test with a single character word
    word = "a"
    expected_pairs = []
    pairs_count = dict(Counter(expected_pairs))
    expected_hash = hashlib.md5(str(pairs_count).encode()).hexdigest()
    assert task_func(word) == expected_hash

    # Test with an empty string
    word = ""
    expected_pairs = []
    pairs_count = dict(Counter(expected_pairs))
    expected_hash = hashlib.md5(str(pairs_count).encode()).hexdigest()
    assert task_func(word) == expected_hash

    # Test with a word that has repeating characters
    word = "bookkeeper"
    expected_pairs = ['bo', 'oo', 'ok', 'ke', 'ee', 'ep', 'pe', 'er']
    pairs_count = dict(Counter(expected_pairs))
    expected_hash = hashlib.md5(str(pairs_count).encode()).hexdigest()
    assert task_func(word) == expected_hash

    # Test with a word that has no repeating consecutive characters
    word = "abcdefg"
    expected_pairs = ['ab', 'bc', 'cd', 'de', 'ef', 'fg']
    pairs_count = dict(Counter(expected_pairs))
    expected_hash = hashlib.md5(str(pairs_count).encode()).hexdigest()
    assert task_func(word) == expected_hash