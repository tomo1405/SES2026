python
import pytest
from src_0306 import task_func

def test_task_func():
    # Test case 1
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    seed = 0
    expected_result = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 10, 'k': 10, 'l': 10, 'm': 10, 'n': 10, 'o': 10, 'p': 10, 'q': 10, 'r': 10, 's': 10, 't': 10, 'u': 10, 'v': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}
    assert task_func(list_of_lists, seed) == expected_result

    # Test case 2
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        []
    ]
    seed = 0
    expected_result = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 10, 'h': 10, 'i': 10, 'j': 10, 'k': 10, 'l': 10, 'm': 10, 'n': 10, 'o': 10, 'p': 10, 'q': 10, 'r': 10, 's': 10, 't': 10, 'u': 10, 'v': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}
    assert task_func(list_of_lists, seed) == expected_result

    # Test case 3
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    seed = 1
    expected_result = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 10, 'k': 10, 'l': 10, 'm': 10, 'n': 10, 'o': 10, 'p': 10, 'q': 10, 'r': 10, 's': 10, 't': 10, 'u': 10, 'v': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}
    assert task_func(list_of_lists, seed) == expected_result

    # Test case 4
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        []
    ]
    seed = 1
    expected_result = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 10, 'h': 10, 'i': 10, 'j': 10, 'k': 10, 'l': 10, 'm': 10, 'n': 10, 'o': 10, 'p': 10, 'q': 10, 'r': 10, 's': 10, 't': 10, 'u': 10, 'v': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}
    assert task_func(list_of_lists, seed) == expected_result