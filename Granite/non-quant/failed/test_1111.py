import pytest
from src_1111 import task_func

def test_task_func():
    word_dict = {"apple": 1, "banana": 2, "cherry": 3}
    expected_result = {"e": 4, "a": 3, "r": 3, "y": 3, "c": 2, "h": 2, "b": 1, "n": 1, "p": 1, "l": 1}
    result = task_func(word_dict)
    assert result == expected_result

def test_task_func_empty_dict():
    word_dict = {}
    expected_result = {}
    result = task_func(word_dict)
    assert result == expected_result

def test_task_func_single_letter():
    word_dict = {"a": 1}
    expected_result = {"a": 1}
    result = task_func(word_dict)
    assert result == expected_result

def test_task_func_multiple_words():
    word_dict = {"apple": 1, "banana": 2, "cherry": 3, "date": 4}
    expected_result = {"e": 6, "a": 4, "r": 4, "t": 4, "y": 4, "c": 3, "h": 3, "b": 2, "n": 2, "p": 1, "l": 1, "d": 1}
    result = task_func(word_dict)
    assert result == expected_result