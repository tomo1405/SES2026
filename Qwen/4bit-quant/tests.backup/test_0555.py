import pytest
from src_0555 import task_func

def test_task_func():
    MIN_WORDS = 3
    MAX_WORDS = 7
    WORDS_POOL = ["apple", "banana", "cherry", "date"]

    # Test with minimum length
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert len(result.split()) >= MIN_WORDS, "Sentence length is less than MIN_WORDS"

    # Test with maximum length
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert len(result.split()) <= MAX_WORDS, "Sentence length is more than MAX_WORDS"

    # Test if all words are in the WORDS_POOL
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    words_in_sentence = set(result.split())
    assert words_in_sentence.issubset(WORDS_POOL), "Sentence contains words not in WORDS_POOL"

    # Test for even and odd length sentences
    for _ in range(10):  # Run multiple times to cover both cases
        result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        words = result.split()
        if len(words) % 2 == 1:
            assert words[len(words) // 2] in WORDS_POOL, "Middle word not in WORDS_POOL"
        else:
            assert words[:len(words) // 2] == words[len(words) // 2:][::-1], "Second half is not the reverse of the first half"

    # Test with different ranges
    MIN_WORDS = 1
    MAX_WORDS = 1
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert len(result.split()) == 1, "Sentence length should be exactly 1"

    MIN_WORDS = 5
    MAX_WORDS = 5
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert len(result.split()) == 5, "Sentence length should be exactly 5"