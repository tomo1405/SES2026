import pytest
from src_0859 import task_func

def test_task_func():
    n = 10
    seed = 1234
    expected_result = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10}
    assert task_func(n, seed) == expected_result

def test_task_func_with_different_seed():
    n = 10
    seed = 5678
    expected_result = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10}
    assert task_func(n, seed) == expected_result

def test_task_func_with_different_n():
    n = 20
    seed = 1234
    expected_result = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13, 'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20}
    assert task_func(n, seed) == expected_result