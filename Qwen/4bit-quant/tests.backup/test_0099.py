import pytest
from src_0099 import task_func
from collections import Counter

def test_task_func():
    # Test with 1 string of length 5
    result = task_func(1, 5)
    assert len(result) == 5  # There should be 5 unique characters at most
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)  # Each item should be a tuple of (char, count)

    # Test with 0 strings
    result = task_func(0, 10)
    assert result == []  # No strings means no characters

    # Test with multiple strings of varying lengths
    result = task_func(5, 3)
    assert len(result) <= 26  # There can't be more than 26 unique lowercase letters
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    # Test with very large number of strings and long length
    result = task_func(100, 100)
    assert len(result) <= 26  # Still, there can't be more than 26 unique lowercase letters

    # Test with a small alphabet size
    result = task_func(10, 1)
    assert len(result) == 10  # Each string is of length 1, so each character is unique

    # Test with a large alphabet size
    result = task_func(1, 26)
    assert len(result) == 26  # All 26 lowercase letters might appear

    # Test with repeated characters
    result = task_func(10, 2)
    counter = Counter(''.join([''.join(random.choices(string.ascii_lowercase, k=2)) for _ in range(10)]))
    assert Counter([item[0] for item in result]) == counter.most_common()

    # Test with a fixed seed for reproducibility
    random.seed(0)
    result1 = task_func(1, 5)
    random.seed(0)
    result2 = task_func(1, 5)
    assert result1 == result2  # Results should be the same with the same seed

    # Test with a large number of strings and a small alphabet size
    result = task_func(1000, 1)
    assert len(result) == 1  # All strings are of length 1, so only one character will be counted