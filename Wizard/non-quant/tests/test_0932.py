python
import pytest
from src_0932 import task_func

def test_task_func():
    # Test case 1
    word = "hello"
    expected_result = {'he': 1, 'el': 1, 'll': 1, 'lo': 1}
    assert task_func(word) == expected_result

    # Test case 2
    word = "abc"
    expected_result = {'ab': 1, 'bc': 1}
    assert task_func(word) == expected_result

    # Test case 3
    word = "aabbcc"
    expected_result = {'aa': 1, 'bb': 1, 'cc': 1, 'ab': 1, 'bc': 1, 'ac': 1}
    assert task_func(word) == expected_result

    # Test case 4
    word = "12345"
    expected_result = {}
    assert task_func(word) == expected_result

    # Test case 5
    word = "a"
    expected_result = {'a': 1}
    assert task_func(word) == expected_result