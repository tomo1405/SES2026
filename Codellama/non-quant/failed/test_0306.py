import pytest
from src_0306 import task_func

def test_task_func_empty_list():
    list_of_lists = [[]]
    seed = 0
    expected_result = Counter({'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10, 'f': 10, 'g': 10, 'h': 10, 'i': 10, 'j': 10})
    assert task_func(list_of_lists, seed) == expected_result

def test_task_func_non_empty_list():
    list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f']]
    seed = 0
    expected_result = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})
    assert task_func(list_of_lists, seed) == expected_result

def test_task_func_multiple_empty_lists():
    list_of_lists = [[], [], []]
    seed = 0
    expected_result = Counter({'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10, 'f': 10, 'g': 10, 'h': 10, 'i': 10, 'j': 10})
    assert task_func(list_of_lists, seed) == expected_result

def test_task_func_multiple_non_empty_lists():
    list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    seed = 0
    expected_result = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1})
    assert task_func(list_of_lists, seed) == expected_result

def test_task_func_different_seeds():
    list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    seed = 1
    expected_result = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1})
    assert task_func(list_of_lists, seed) == expected_result

def test_task_func_different_alphabet():
    list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    seed = 0
    expected_result = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1})
    assert task_func(list_of_lists, seed) == expected_result