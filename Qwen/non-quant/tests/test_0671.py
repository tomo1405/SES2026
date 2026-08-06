import pytest
from src_0671 import task_func

def test_task_func():
    # Test with an empty string
    assert task_func("", {}) == ""

    # Test with a single character
    assert task_func("a", {"a": 1}) == "a"
    assert task_func("a", {}) == ""

    # Test with multiple characters and weights
    assert task_func("abc", {"a": 1, "b": 2, "c": 3}) == "abc"
    assert task_func("abc", {"a": 3, "b": 2, "c": 1}) == "a"

    # Test with repeated characters
    assert task_func("aabbcc", {"a": 1, "b": 2, "c": 3}) == "bbcc"
    assert task_func("aabbcc", {"a": 3, "b": 2, "c": 1}) == "aaa"

    # Test with negative weights
    assert task_func("abc", {"a": -1, "b": -2, "c": -3}) == ""
    assert task_func("abc", {"a": -3, "b": -2, "c": -1}) == "a"

    # Test with mixed positive and negative weights
    assert task_func("abc", {"a": 1, "b": -2, "c": 3}) == "ac"
    assert task_func("abc", {"a": -1, "b": 2, "c": -3}) == "b"

    # Test with non-contiguous characters
    assert task_func("abcde", {"a": 1, "c": 3, "e": 5}) == "ace"
    assert task_func("abcde", {"a": 5, "c": 1, "e": 3}) == "ae"

    # Test with large input
    long_str = "a" * 1000 + "b" * 1000 + "c" * 1000
    weights = {"a": 1, "b": 2, "c": 3}
    assert task_func(long_str, weights) == "b" * 1000 + "c" * 1000

    # Test with no valid substrings
    assert task_func("abc", {"d": 4, "e": 5, "f": 6}) == ""