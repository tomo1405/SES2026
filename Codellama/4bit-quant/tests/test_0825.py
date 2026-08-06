import pytest
from src_0825 import task_func

def test_task_func():
    # Test case 1: No punctuation
    text = "This is a sentence"
    expected_words = 4
    expected_punctuation = 0
    assert task_func(text) == (expected_words, expected_punctuation)

    # Test case 2: With punctuation
    text = "This, is a sentence!"
    expected_words = 4
    expected_punctuation = 2
    assert task_func(text) == (expected_words, expected_punctuation)

    # Test case 3: With multiple punctuation
    text = "This, is a sentence!?"
    expected_words = 4
    expected_punctuation = 3
    assert task_func(text) == (expected_words, expected_punctuation)

    # Test case 4: With special characters
    text = "This, is a sentence!?$"
    expected_words = 4
    expected_punctuation = 4
    assert task_func(text) == (expected_words, expected_punctuation)

    # Test case 5: With numbers
    text = "This, is a sentence!?$123"
    expected_words = 5
    expected_punctuation = 5
    assert task_func(text) == (expected_words, expected_punctuation)