import pytest
from src_0934 import task_func

def test_task_func():
    # Test case 1: Single letter
    word = "a"
    expected_result = [("a", 1)], ["a"]
    assert task_func(word) == expected_result

    # Test case 2: Multiple letters
    word = "hello"
    expected_result = [("h", 1), ("e", 2), ("l", 3), ("l", 4), ("o", 5)], ["hello"]
    assert task_func(word) == expected_result

    # Test case 3: Word with special characters
    word = "hello world"
    expected_result = [("h", 1), ("e", 2), ("l", 3), ("l", 4), ("o", 5), (" ", 6), ("w", 7), ("o", 8), ("r", 9), ("l", 10), ("d", 11)], ["hello world"]
    assert task_func(word) == expected_result

    # Test case 4: Word with numbers
    word = "hello123"
    expected_result = [("h", 1), ("e", 2), ("l", 3), ("l", 4), ("o", 5), ("1", 6), ("2", 7), ("3", 8)], ["hello123"]
    assert task_func(word) == expected_result

    # Test case 5: Word with special characters and numbers
    word = "hello123 world"
    expected_result = [("h", 1), ("e", 2), ("l", 3), ("l", 4), ("o", 5), ("1", 6), ("2", 7), ("3", 8), (" ", 9), ("w", 10), ("o", 11), ("r", 12), ("l", 13), ("d", 14)], ["hello123 world"]
    assert task_func(word) == expected_result