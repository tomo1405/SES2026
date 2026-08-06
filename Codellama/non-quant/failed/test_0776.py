import pytest
from src_0776 import task_func

def test_task_func():
    # Test case 1: No hyphen in the input string
    input_string = "abcdefghijklmnopqrstuvwxyz"
    expected_result = {letter: 1 for letter in ascii_lowercase}
    assert task_func(input_string) == expected_result

    # Test case 2: Hyphen in the input string
    input_string = "abc-defghijklmnopqrstuvwxyz"
    expected_result = {letter: 1 for letter in ascii_lowercase}
    expected_result["a"] = 0
    assert task_func(input_string) == expected_result

    # Test case 3: Input string with multiple hyphens
    input_string = "abc-def-ghijklmnopqrstuvwxyz"
    expected_result = {letter: 1 for letter in ascii_lowercase}
    expected_result["a"] = 0
    expected_result["d"] = 0
    assert task_func(input_string) == expected_result

    # Test case 4: Input string with non-letter characters
    input_string = "abc-def-ghijklmnopqrstuvwxyz123"
    expected_result = {letter: 1 for letter in ascii_lowercase}
    expected_result["a"] = 0
    expected_result["d"] = 0
    assert task_func(input_string) == expected_result

    # Test case 5: Input string with letters only
    input_string = "abcdefghijklmnopqrstuvwxyz"
    expected_result = {letter: 1 for letter in ascii_lowercase}
    assert task_func(input_string) == expected_result