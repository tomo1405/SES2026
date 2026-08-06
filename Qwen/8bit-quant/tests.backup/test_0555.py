import pytest
from src_0555 import task_func

def test_task_func():
    MIN_WORDS = 3
    MAX_WORDS = 7
    WORDS_POOL = ["apple", "banana", "cherry", "date", "elderberry"]

    # Test with minimum length
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    words = sentence.split()
    assert len(words) >= MIN_WORDS and len(words) <= MAX_WORDS
    assert all(word in WORDS_POOL for word in words)

    # Test with maximum length
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    words = sentence.split()
    assert len(words) >= MIN_WORDS and len(words) <= MAX_WORDS
    assert all(word in WORDS_POOL for word in words)

    # Test with odd length
    sentence = task_func(5, 5, WORDS_POOL)
    words = sentence.split()
    assert len(words) == 5
    assert all(word in WORDS_POOL for word in words)
    assert words[0] == words[-1]
    assert words[1] == words[-2]
    assert words[2] == words[-3]

    # Test with even length
    sentence = task_func(4, 4, WORDS_POOL)
    words = sentence.split()
    assert len(words) == 4
    assert all(word in WORDS_POOL for word in words)
    assert words[0] == words[-1]
    assert words[1] == words[-2]

    # Test with different word pools
    WORDS_POOL_2 = ["cat", "dog", "elephant"]
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL_2)
    words = sentence.split()
    assert len(words) >= MIN_WORDS and len(words) <= MAX_WORDS
    assert all(word in WORDS_POOL_2 for word in words)