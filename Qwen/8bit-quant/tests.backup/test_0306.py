import pytest
from src_0306 import task_func
from collections import Counter

def test_task_func_with_non_empty_lists():
    input_data = [['a', 'b'], ['c', 'd']]
    expected_output = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_lists():
    input_data = [[], ['e', 'f'], [], ['g']]
    expected_output = Counter({'e': 1, 'f': 1, 'g': 1})
    assert task_func(input_data) == expected_output

def test_task_func_with_no_lists():
    input_data = []
    expected_output = Counter()
    assert task_func(input_data) == expected_output

def test_task_func_with_all_empty_lists():
    input_data = [[], [], []]
    expected_output = Counter()
    assert task_func(input_data) == expected_output

def test_task_func_with_mixed_lists():
    input_data = [['h', 'i', 'j'], [], ['k'], ['l', 'm', 'n', 'o'], []]
    expected_output = Counter({'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1})
    assert task_func(input_data) == expected_output

def test_task_func_with_seed():
    input_data = [[], []]
    expected_output = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1})
    assert task_func(input_data, seed=0) == expected_output

def test_task_func_with_different_seed():
    input_data = [[], []]
    expected_output = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1})
    assert task_func(input_data, seed=1) != expected_output