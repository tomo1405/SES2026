import pytest
from src_0005 import task_func

def test_task_func():
    d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    expected_result = {'a': 3, 'b': 3, 'c': 3}
    assert task_func(d) == expected_result

def test_task_func_empty_dict():
    d = {}
    expected_result = {}
    assert task_func(d) == expected_result

def test_task_func_empty_list():
    d = {'a': []}
    expected_result = {'a': 0}
    assert task_func(d) == expected_result

def test_task_func_duplicate_keys():
    d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'a': [10, 11, 12]}
    expected_result = {'a': 6, 'b': 3, 'c': 3}
    assert task_func(d) == expected_result