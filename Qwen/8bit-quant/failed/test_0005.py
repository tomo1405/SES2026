import pytest
from src_0005 import task_func
from collections import Counter

def test_task_func_with_empty_dict():
    assert task_func({}) == {}

def test_task_func_with_single_key_value_pair():
    assert task_func({'a': ['x', 'y']}) == {'x': 1, 'y': 1}

def test_task_func_with_multiple_keys():
    assert task_func({'a': ['x', 'y'], 'b': ['x', 'z']}) == {'x': 2, 'y': 1, 'z': 1}

def test_task_func_with_nested_lists():
    assert task_func({'a': [['x', 'y'], ['x']], 'b': ['z']}) == {'x': 2, 'y': 1, 'z': 1}

def test_task_func_with_empty_lists():
    assert task_func({'a': [], 'b': []}) == {}

def test_task_func_with_identical_elements():
    assert task_func({'a': ['x', 'x', 'x'], 'b': ['x']}) == {'x': 4}

def test_task_func_with_no_common_elements():
    assert task_func({'a': ['x'], 'b': ['y'], 'c': ['z']}) == {'x': 1, 'y': 1, 'z': 1}