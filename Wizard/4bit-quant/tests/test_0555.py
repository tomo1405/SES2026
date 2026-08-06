python
import numpy as np
import random
import pytest

def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
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

    return ' '.join(sentence)

def test_task_func():
    # Test case 1
    MIN_WORDS = 1
    MAX_WORDS = 5
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 4
    assert sentence.split()[0] in WORDS_POOL
    assert sentence.split()[1] in WORDS_POOL
    assert sentence.split()[2] in WORDS_POOL
    assert sentence.split()[3] in WORDS_POOL
    assert sentence.split()[4] in WORDS_POOL

    # Test case 2
    MIN_WORDS = 5
    MAX_WORDS = 10
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 9
    assert sentence.split()[0] in WORDS_POOL
    assert sentence.split()[1] in WORDS_POOL
    assert sentence.split()[2] in WORDS_POOL
    assert sentence.split()[3] in WORDS_POOL
    assert sentence.split()[4] in WORDS_POOL
    assert sentence.split()[5] in WORDS_POOL
    assert sentence.split()[6] in WORDS_POOL
    assert sentence.split()[7] in WORDS_POOL
    assert sentence.split()[8] in WORDS_POOL
    assert sentence.split()[9] in WORDS_POOL

    # Test case 3
    MIN_WORDS = 1
    MAX_WORDS = 1
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 0
    assert sentence.split()[0] in WORDS_POOL

    # Test case 4
    MIN_WORDS = 1
    MAX_WORDS = 1
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 0
    assert sentence.split()[0] in WORDS_POOL

    # Test case 5
    MIN_WORDS = 1
    MAX_WORDS = 1
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 0
    assert sentence.split()[0] in WORDS_POOL

    # Test case 6
    MIN_WORDS = 1
    MAX_WORDS = 1
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 0
    assert sentence.split()[0] in WORDS_POOL

    # Test case 7
    MIN_WORDS = 1
    MAX_WORDS = 1
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 0
    assert sentence.split()[0] in WORDS_POOL

    # Test case 8
    MIN_WORDS = 1
    MAX_WORDS = 1
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 0
    assert sentence.split()[0] in WORDS_POOL

    # Test case 9
    MIN_WORDS = 1
    MAX_WORDS = 1
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 0
    assert sentence.split()[0] in WORDS_POOL

    # Test case 10
    MIN_WORDS = 1
    MAX_WORDS = 1
    WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert sentence.count(' ') == 0
    assert sentence.split()[0] in WORDS_POOL