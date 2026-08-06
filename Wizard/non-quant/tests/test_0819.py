python
import re
import string
import pytest

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    words = re.split(r'\s+', text)
    cleaned_words = [re.sub(f'[{PUNCTUATION}]', '', word).lower() for word in words]

    return cleaned_words

def test_task_func():
    # Test case 1
    text = "Hello, World!"
    expected_output = ["hello", "world"]
    assert task_func(text) == expected_output

    # Test case 2
    text = "Python is awesome!"
    expected_output = ["python", "is", "awesome"]
    assert task_func(text) == expected_output

    # Test case 3
    text = "This is a test. Testing, 1, 2, 3."
    expected_output = ["this", "is", "a", "test", "testing", "1", "2", "3"]
    assert task_func(text) == expected_output