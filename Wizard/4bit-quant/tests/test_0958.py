python
import string
import re
import pytest

def task_func(text: str) -> tuple:
    words = text.split()
    chars = re.sub("\s", "", re.sub(f"[{string.punctuation}]", "", text))

    return len(words), len(chars), len(set(chars))

def test_task_func():
    # Test case 1
    text = "Hello, World!"
    expected_result = (2, 10, 10)
    assert task_func(text) == expected_result

    # Test case 2
    text = "The quick brown fox jumps over the lazy dog."
    expected_result = (9, 32, 26)
    assert task_func(text) == expected_result

    # Test case 3
    text = "1234567890"
    expected_result = (1, 10, 10)
    assert task_func(text) == expected_result

    # Test case 4
    text = ""
    expected_result = (0, 0, 0)
    assert task_func(text) == expected_result