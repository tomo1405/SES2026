python
import string
import re
import pytest

def task_func(text: str) -> tuple:
    words = text.split()
    chars = re.sub("\s", "", re.sub(f"[{string.punctuation}]", "", text))

    return len(words), len(chars), len(set(chars))

def test_task_func():
    assert task_func("Hello, world!") == (2, 12, 10)
    assert task_func("The quick brown fox jumps over the lazy dog.") == (9, 41, 26)
    assert task_func("Python is a great language!") == (4, 32, 24)