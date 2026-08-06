import pytest
from collections import Counter
import itertools
from src_0005 import task_func

def test_task_func():
    d = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
    expected_output = {'1': 1, '2': 2, '3': 3, '4': 2, '5': 1}
    actual_output = task_func(d)
    assert actual_output == expected_output

def test_task_func_empty_dict():
    d = {}
    expected_output = {}
    actual_output = task_func(d)
    assert actual_output == expected_output

def test_task_func_single_key():
    d = {'a': [1]}
    expected_output = {'1': 1}
    actual_output = task_func(d)
    assert actual_output == expected_output

def test_task_func_multiple_keys():
    d = {'a': [1, 2], 'b': [2, 3]}
    expected_output = {'1': 1, '2': 2, '3': 1}
    actual_output = task_func(d)
    assert actual_output == expected_output