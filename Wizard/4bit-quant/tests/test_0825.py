python
import re
import string
import pytest

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Use a regex that matches sequences of alphanumeric characters as words
    words = re.findall(r'\b\w+\b', text)
    punctuation_marks = [char for char in text if char in PUNCTUATION]

    return len(words), len(punctuation_marks)

def test_task_func():
    # Test case 1
    text = "This is a test sentence. It has some punctuation marks!"
    expected_result = (5, 16)
    assert task_func(text) == expected_result

    # Test case 2
    text = "This is a test sentence with no punctuation marks."
    expected_result = (5, 0)
    assert task_func(text) == expected_result

    # Test case 3
    text = "This is a test sentence with no words."
    expected_result = (0, 0)
    assert task_func(text) == expected_result