import pytest
from src_0934 import task_func
import wordninja

def test_task_func():
    # Test case 1: Simple word
    result = task_func("hello")
    expected_tuples = [('h', 8), ('e', 5), ('l', 12), ('l', 12), ('o', 15)]
    expected_split = ['hello']
    assert result == (expected_tuples, expected_split)

    # Test case 2: Word with multiple words when split
    result = task_func("thisisatest")
    expected_tuples = [('t', 20), ('h', 8), ('i', 9), ('s', 19), ('i', 9), ('s', 19), ('a', 1), ('t', 20), ('e', 5), ('s', 19), ('t', 20)]
    expected_split = ['this', 'is', 'a', 'test']
    assert result == (expected_tuples, expected_split)

    # Test case 3: Single character
    result = task_func("a")
    expected_tuples = [('a', 1)]
    expected_split = ['a']
    assert result == (expected_tuples, expected_split)

    # Test case 4: Empty string
    result = task_func("")
    expected_tuples = []
    expected_split = []
    assert result == (expected_tuples, expected_split)

    # Test case 5: Word with numbers and special characters (should ignore non-alphabetic characters)
    result = task_func("h3ll0!")
    expected_tuples = [('h', 8), ('l', 12), ('l', 12), ('o', 15)]
    expected_split = ['hello']
    assert result == (expected_tuples, expected_split)

    # Test case 6: Word with uppercase letters (should be treated as lowercase)
    result = task_func("HELLO")
    expected_tuples = [('h', 8), ('e', 5), ('l', 12), ('l', 12), ('o', 15)]
    expected_split = ['hello']
    assert result == (expected_tuples, expected_split)