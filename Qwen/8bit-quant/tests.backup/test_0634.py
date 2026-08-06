import pytest
from src_0634 import task_func
import re
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
stopwords.ensure_loaded()

def test_task_func():
    # Test with empty string
    assert task_func("") == {}

    # Test with single word
    assert task_func("hello") == {}

    # Test with multiple words including stopwords
    assert task_func("hello world hello") == {"world": 1}

    # Test with punctuation
    assert task_func("Hello, world! Hello.") == {"world": 1}

    # Test with case insensitivity
    assert task_func("Hello hello HELLO") == {}

    # Test with no stopwords
    assert task_func("unique words only") == {"unique": 1, "words": 1, "only": 1}

    # Test with duplicate words after removing stopwords
    assert task_func("a quick brown fox jumps over the lazy dog a quick brown") == {
        "fox": 1,
        "jumps": 1,
        "lazy": 1,
        "dog": 1,
        "over": 1,
        "the": 1
    }

    # Test with numbers
    assert task_func("123 456 789") == {}

    # Test with special characters
    assert task_func("!@# $%^ &*()") == {}

    # Test with mixed content
    assert task_func("Test this, test that! Testing is fun.") == {
        "test": 1,
        "this": 1,
        "that": 1,
        "testing": 1,
        "is": 1,
        "fun": 1
    }