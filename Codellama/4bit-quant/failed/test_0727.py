import pytest
from src_0727 import task_func

def test_task_func():
    # Test case 1: No English words
    s = "This is a sentence with no English words."
    n = 5
    expected = []
    assert task_func(s, n) == expected

    # Test case 2: All English words
    s = "This is a sentence with only English words."
    n = 5
    expected = ["This", "is", "a", "sentence", "with"]
    assert task_func(s, n) == expected

    # Test case 3: Partial English words
    s = "This is a sentence with some English words."
    n = 5
    expected = ["This", "is", "a", "sentence", "with"]
    assert task_func(s, n) == expected

    # Test case 4: No input
    s = ""
    n = 5
    expected = []
    assert task_func(s, n) == expected

    # Test case 5: No input
    s = None
    n = 5
    expected = []
    assert task_func(s, n) == expected

    # Test case 6: Invalid input
    s = 123
    n = 5
    expected = []
    assert task_func(s, n) == expected

    # Test case 7: Invalid input
    s = [1, 2, 3]
    n = 5
    expected = []
    assert task_func(s, n) == expected

    # Test case 8: Invalid input
    s = {"a": 1, "b": 2}
    n = 5
    expected = []
    assert task_func(s, n) == expected

    # Test case 9: Invalid input
    s = True
    n = 5
    expected = []
    assert task_func(s, n) == expected

    # Test case 10: Invalid input
    s = False
    n = 5
    expected = []
    assert task_func(s, n) == expected