import pytest
from src_0776 import task_func

def test_task_func():
    # Test case 1: No hyphen
    string = "abcdefghijklmnopqrstuvwxyz"
    expected_result = {letter: 1 for letter in ascii_lowercase}
    assert task_func(string) == expected_result

    # Test case 2: Hyphen
    string = "abcdefghijklmnopqrstuvwxyz-a"
    expected_result = {letter: 1 for letter in ascii_lowercase}
    assert task_func(string) == expected_result

    # Test case 3: Non-letter characters
    string = "abcdefghijklmnopqrstuvwxyz-1"
    expected_result = {letter: 1 for letter in ascii_lowercase}
    assert task_func(string) == expected_result

    # Test case 4: Empty string
    string = ""
    expected_result = {letter: 0 for letter in ascii_lowercase}
    assert task_func(string) == expected_result

    # Test case 5: Non-string input
    string = 123
    expected_result = {letter: 0 for letter in ascii_lowercase}
    assert task_func(string) == expected_result