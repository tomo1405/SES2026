import pytest
from src_0671 import task_func

def test_task_func():
    # Test case 1: Simple case with positive weights
    x = "abc"
    w = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(x, w) == "abc"

    # Test case 2: Case with negative weights
    x = "abc"
    w = {'a': -1, 'b': -2, 'c': -3}
    assert task_func(x, w) == ""

    # Test case 3: Mixed weights
    x = "abc"
    w = {'a': 1, 'b': -2, 'c': 3}
    assert task_func(x, w) == "ac"

    # Test case 4: Single character string
    x = "a"
    w = {'a': 10}
    assert task_func(x, w) == "a"

    # Test case 5: Empty string
    x = ""
    w = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(x, w) == ""

    # Test case 6: No matching characters in weight dictionary
    x = "xyz"
    w = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(x, w) == ""

    # Test case 7: All characters have the same weight
    x = "aaa"
    w = {'a': 1}
    assert task_func(x, w) == "aaa"

    # Test case 8: Different weights for different substrings of the same length
    x = "abcd"
    w = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert task_func(x, w) == "abcd"

    # Test case 9: Substring with zero weight
    x = "abc"
    w = {'a': 1, 'b': 0, 'c': 3}
    assert task_func(x, w) == "ac"

    # Test case 10: Substring with negative and zero weights
    x = "abc"
    w = {'a': -1, 'b': 0, 'c': -3}
    assert task_func(x, w) == ""