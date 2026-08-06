python
import pandas as pd
import regex as re
import pytest

# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]

def task_func(text):
    words = re.findall(r"\b\w+\b", text.lower())
    words = [word for word in words if word not in STOPWORDS]
    word_counts = pd.Series(words).value_counts().rename(None)
    return word_counts

def test_task_func():
    # Test case 1
    text = "The quick brown fox jumps over the lazy dog."
    expected_result = pd.Series({"quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1})
    assert task_func(text).equals(expected_result)

    # Test case 2
    text = "The quick brown fox jumps over the lazy dog. The dog is not amused."
    expected_result = pd.Series({"quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 2})
    assert task_func(text).equals(expected_result)

    # Test case 3
    text = "The quick brown fox jumps over the lazy dog. The dog is not amused. The dog is not amused."
    expected_result = pd.Series({"quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 3})
    assert task_func(text).equals(expected_result)

    # Test case 4
    text = "The quick brown fox jumps over the lazy dog. The dog is not amused. The dog is not amused. The dog is not amused."
    expected_result = pd.Series({"quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 4})
    assert task_func(text).equals(expected_result)

    # Test case 5
    text = "The quick brown fox jumps over the lazy dog. The dog is not amused. The dog is not amused. The dog is not amused. The dog is not amused."
    expected_result = pd.Series({"quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 5})
    assert task_func(text).equals(expected_result)