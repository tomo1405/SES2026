import pytest
from src_0903 import task_func
from collections import Counter

def test_task_func_with_all_keys():
    data = {'x': [1, 2, 2, 3], 'y': [4, 5, 5, 6], 'z': [7, 8, 8, 9]}
    expected_output = {
        'x': Counter({2: 2, 1: 1, 3: 1}),
        'y': Counter({5: 2, 4: 1, 6: 1}),
        'z': Counter({8: 2, 7: 1, 9: 1})
    }
    assert task_func(data) == expected_output

def test_task_func_with_missing_keys():
    data = {'x': [1, 2, 2, 3], 'y': [4, 5, 5, 6]}
    expected_output = {
        'x': Counter({2: 2, 1: 1, 3: 1}),
        'y': Counter({5: 2, 4: 1, 6: 1}),
        'z': Counter()
    }
    assert task_func(data) == expected_output

def test_task_func_with_empty_data():
    data = {}
    expected_output = {
        'x': Counter(),
        'y': Counter(),
        'z': Counter()
    }
    assert task_func(data) == expected_output

def test_task_func_with_no_data():
    data = {'a': [], 'b': []}
    expected_output = {
        'x': Counter(),
        'y': Counter(),
        'z': Counter()
    }
    assert task_func(data) == expected_output

def test_task_func_with_nan_values():
    import numpy as np
    data = {'x': [1, 2, np.nan, 3], 'y': [np.nan, 5, 5, 6], 'z': [7, 8, 8, np.nan]}
    expected_output = {
        'x': Counter({2: 1, 1: 1, 3: 1}),
        'y': Counter({5: 2, 6: 1}),
        'z': Counter({8: 2, 7: 1})
    }
    assert task_func(data) == expected_output