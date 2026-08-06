import pytest
from src_0671 import task_func

def test_task_func():
    # Test case 1: Basic test with positive weights
    x = "abc"
    w = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(x, w) == "abc"

    # Test case 2: Substring with higher weight
    x = "abc"
    w = {'a': 1, 'b': 2, 'c': 1}
    assert task_func(x, w) == "ab"

    # Test case 3: Single character substring
    x = "a"
    w = {'a': 5}
    assert task_func(x, w) == "a"

    # Test case 4: Empty string
    x = ""
    w = {'a': 1, 'b': 2}
    assert task_func(x, w) == ""

    # Test case 5: No matching characters
    x = "abc"
    w = {'d': 1, 'e': 2}
    assert task_func(x, w) == ""

    # Test case 6: All characters have zero weight
    x = "abc"
    w = {'a': 0, 'b': 0, 'c': 0}
    assert task_func(x, w) == ""

    # Test case 7: Mixed weights including negative
    x = "abc"
    w = {'a': 1, 'b': -1, 'c': 2}
    assert task_func(x, w) == "ac"

    # Test case 8: Long string with repeating characters
    x = "aabbbcc"
    w = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(x, w) == "bbb"

    # Test case 9: String with spaces and special characters
    x = "a b!c"
    w = {'a': 1, ' ': 2, 'b': 3, '!': 4, 'c': 5}
    assert task_func(x, w) == "b!c"

    # Test case 10: String with multiple substrings of same weight
    x = "abcabc"
    w = {'a': 1, 'b': 1, 'c': 1}
    assert task_func(x, w) == "abcabc"  # The first occurrence is returned