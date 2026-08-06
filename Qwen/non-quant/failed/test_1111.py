import pytest
from src_1111 import task_func
from collections import Counter
from operator import itemgetter
import itertools

def test_task_func_with_unique_letters():
    word_dict = {'apple': 1, 'banana': 1}
    expected_output = {'a': 3, 'p': 2, 'l': 1, 'e': 1, 'b': 1, 'n': 1}
    assert task_func(word_dict) == expected_output

def test_task_func_with_repeated_letters():
    word_dict = {'hello': 1, 'world': 1}
    expected_output = {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}
    assert task_func(word_dict) == expected_output

def test_task_func_with_empty_dict():
    word_dict = {}
    expected_output = {}
    assert task_func(word_dict) == expected_output

def test_task_func_with_single_word():
    word_dict = {'python': 1}
    expected_output = {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
    assert task_func(word_dict) == expected_output

def test_task_func_with_multiple_same_words():
    word_dict = {'test': 3, 'case': 2}
    expected_output = {'t': 5, 'e': 3, 's': 2, 'c': 1, 'a': 1}
    assert task_func(word_dict) == expected_output