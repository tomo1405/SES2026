import pytest
from src_0912 import task_func

def test_task_func():
    # Test case 1: Empty list
    letters = []
    expected_result = 1
    assert task_func(letters) == expected_result

    # Test case 2: Single letter
    letters = ['A']
    expected_result = 1
    assert task_func(letters) == expected_result

    # Test case 3: Multiple letters
    letters = ['A', 'B', 'C']
    expected_result = 6
    assert task_func(letters) == expected_result

    # Test case 4: Invalid input
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|', '\\', ';', ':', '"', '\'', ',', '<', '.', '>', '/', '?']
    expected_result = 1
    assert task_func(letters) == expected_result