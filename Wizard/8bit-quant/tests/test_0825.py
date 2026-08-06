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
    text = "Hello, world!"
    expected_result = (1, 3)
    assert task_func(text) == expected_result

    # Test case 2
    text = "This is a test string."
    expected_result = (4, 1)
    assert task_func(text) == expected_result

    # Test case 3
    text = "12345"
    expected_result = (1, 0)
    assert task_func(text) == expected_result

    # Test case 4
    text = "!"
    expected_result = (0, 1)
    assert task_func(text) == expected_result