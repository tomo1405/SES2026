python
import re
import string
import pytest

def task_func(text1, text2):
    # Constants
    PUNCTUATION = string.punctuation

    cleaned_texts = []

    # Remove punctuation from each text string
    for text in [text1, text2]:
        cleaned_text = re.sub('['+re.escape(PUNCTUATION)+']', '', text)
        cleaned_texts.append(cleaned_text)

    return tuple(cleaned_texts)

def test_task_func():
    # Test case 1
    text1 = "Hello, World!"
    text2 = "Python is awesome!"
    expected_output = ("Hello World", "Python is awesome")
    assert task_func(text1, text2) == expected_output

    # Test case 2
    text1 = "This is a test string."
    text2 = "Another test string."
    expected_output = ("This is a test string", "Another test string")
    assert task_func(text1, text2) == expected_output

    # Test case 3
    text1 = "12345"
    text2 = "67890"
    expected_output = ("12345", "67890")
    assert task_func(text1, text2) == expected_output

    # Test case 4
    text1 = "!"
    text2 = "?"
    expected_output = ("", "")
    assert task_func(text1, text2) == expected_output