import pytest
from src_0903 import task_func
from collections import Counter

def test_task_func_with_all_keys():
    data = {'x': [1, 2, 2, 3], 'y': [4, 5, 5, 5], 'z': [6, 7, 8, 8]}
    expected = {
        'x': Counter({2: 2, 1: 1, 3: 1}),
        'y': Counter({5: 3, 4: 1}),
        'z': Counter({8: 2, 6: 1, 7: 1})
    }
    assert task_func(data) == expected

def test_task_func_with_missing_key():
    data = {'x': [1, 2, 2, 3], 'y': [4, 5, 5, 5]}
    expected = {
        'x': Counter({2: 2, 1: 1, 3: 1}),
        'y': Counter({5: 3, 4: 1}),
        'z': Counter()
    }
    assert task_func(data) == expected

def test_task_func_with_empty_data():
    data = {}
    expected = {
        'x': Counter(),
        'y': Counter(),
        'z': Counter()
    }
    assert task_func(data) == expected

def test_task_func_with_all_null_values():
    data = {'x': [None, None, None], 'y': [None, None, None], 'z': [None, None, None]}
    expected = {
        'x': Counter(),
        'y': Counter(),
        'z': Counter()
    }
    assert task_func(data) == expected

def test_task_func_with_mixed_data_types():
    data = {'x': [1, 'a', 2, 'b'], 'y': [3, 3, 4, 4], 'z': [5, 6, 7, 8]}
    expected = {
        'x': Counter({'a': 1, 'b': 1, 1: 1, 2: 1}),
        'y': Counter({3: 2, 4: 2}),
        'z': Counter({5: 1, 6: 1, 7: 1, 8: 1})
    }
    assert task_func(data) == expected