import pytest
from src_0934 import task_func

def test_task_func():
    # Test case 1:
    word = "hello"
    expected_result = [('h', 8), ('e', 5), ('l', 11), ('l', 11), ('o', 15)]
    assert task_func(word) == expected_result

    # Test case 2:
    word = "world"
    expected_result = [('w', 23), ('o', 15), ('r', 18), ('l', 11), ('d', 4)]
    assert task_func(word) == expected_result

    # Test case 3:
    word = "python"
    expected_result = [('p', 16), ('y', 25), ('t', 20), ('h', 8), ('o', 15), ('n', 14)]
    assert task_func(word) == expected_result