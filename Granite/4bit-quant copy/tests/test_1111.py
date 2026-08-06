import pytest
from collections import Counter
from operator import itemgetter
import itertools

def task_func(word_dict):
    letters = list(itertools.chain.from_iterable(word_dict.keys()))
    count_dict = dict(Counter(letters))
    sorted_dict = dict(sorted(count_dict.items(), key=itemgetter(1), reverse=True))
    return sorted_dict

def test_task_func():
    word_dict = {"apple": 1, "banana": 2, "cherry": 3}
    expected_result = {"a": 3, "p": 1, "l": 1, "e": 1, "b": 1, "n": 1, "c": 1, "h": 1, "r": 1, "y": 1}
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

def test_task_func_multiple_counts():
    word_dict = {"apple": 1, "banana": 2, "cherry": 3, "date": 2, "elderberry": 4}
    expected_result = {"a": 6, "p": 1, "l": 2, "e": 2, "b": 2, "n": 2, "c": 1, "h": 2, "r": 2, "y": 2, "d": 1, "t": 1}
    result = task_func(word_dict)
    assert result == expected_result