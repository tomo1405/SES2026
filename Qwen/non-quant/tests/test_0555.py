import pytest
from src_0555 import task_func

# Mocking numpy and random for consistent results
import numpy as np
import random

@pytest.fixture
def mock_random(monkeypatch):
    def mock_randint(a, b):
        return 3  # Fixed length for easier testing

    def mock_choice(seq):
        return "testword"  # Fixed word for easier testing

    monkeypatch.setattr(np.random, 'randint', mock_randint)
    monkeypatch.setattr(random, 'choice', mock_choice)

def test_task_func_with_even_length(mock_random):
    MIN_WORDS = 2
    MAX_WORDS = 4
    WORDS_POOL = ["word1", "word2", "word3"]
    
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert result == "testword testword"

def test_task_func_with_odd_length(mock_random):
    MIN_WORDS = 3
    MAX_WORDS = 5
    WORDS_POOL = ["word1", "word2", "word3"]
    
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert result == "testword testword testword testword"

def test_task_func_min_max_same(mock_random):
    MIN_WORDS = 4
    MAX_WORDS = 4
    WORDS_POOL = ["word1", "word2", "word3"]
    
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert result == "testword testword testword testword"

def test_task_func_with_single_word_pool(mock_random):
    MIN_WORDS = 2
    MAX_WORDS = 4
    WORDS_POOL = ["singleword"]
    
    result = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    assert result == "singleword singleword"