import pytest
from src_1111 import task_func

def test_task_func():
    word_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    expected_result = {'e': 4, 'a': 3, 'r': 3, 'y': 3, 'p': 2, 'c': 1, 'h': 1, 'b': 1, 'n': 1, 'i': 1, 'l': 1, 't': 1}
    result = task_func(word_dict)
    assert result == expected_result

def test_task_func_empty_dict():
    word_dict = {}
    expected_result = {}
    result = task_func(word_dict)
    assert result == expected_result

def test_task_func_single_letter():
    word_dict = {'a': 1}
    expected_result = {'a': 1}
    result = task_func(word_dict)
    assert result == expected_result

def test_task_func_multiple_words():
    word_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4, 'elderberry': 5}
    expected_result = {'e': 7, 'a': 6, 'r': 6, 'y': 6, 'p': 4, 'c': 3, 'h': 3, 'b': 3, 'n': 3, 'i': 3, 'l': 2, 't': 2, 'd': 1}
    result = task_func(word_dict)
    assert result == expected_result