python
import pytest
from src_0932 import task_func

def test_task_func():
    # Test case 1
    word = "hello"
    expected_result = {'he': 1, 'el': 1, 'll': 1, 'ho': 1, 'oh': 1}
    assert task_func(word) == expected_result

    # Test case 2
    word = "abc"
    expected_result = {'ab': 1, 'bc': 1}
    assert task_func(word) == expected_result

    # Test case 3
    word = "aabbcc"
    expected_result = {'aa': 1, 'bb': 1, 'cc': 1, 'ab': 1, 'bc': 1}
    assert task_func(word) == expected_result

    # Test case 4
    word = "123"
    expected_result = {}
    assert task_func(word) == expected_result

    # Test case 5
    word = "a"
    expected_result = {'a': 1}
    assert task_func(word) == expected_result

    # Test case 6
    word = "aaabbbccc"
    expected_result = {'aaa': 1, 'bbb': 1, 'ccc': 1, 'aab': 1, 'bbc': 1, 'cca': 1, 'abb': 1, 'bcc': 1, 'caa': 1, 'aba': 1, 'bba': 1, 'caa': 1, 'abb': 1, 'bcc': 1, 'caa': 1}
    assert task_func(word) == expected_result