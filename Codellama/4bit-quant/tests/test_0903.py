from typing import Counter

import pytest
from src_0903 import task_func


def test_task_func():
    d = {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5], 'z': [1, 2, 3, 4, 5]}
    counts = task_func(d)
    assert counts == {'x': Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
                     'y': Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
                     'z': Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})}

def test_task_func_missing_column():
    d = {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5]}
    counts = task_func(d)
    assert counts == {'x': Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
                     'y': Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
                     'z': Counter()}

def test_task_func_empty_column():
    d = {'x': [], 'y': [], 'z': []}
    counts = task_func(d)
    assert counts == {'x': Counter(), 'y': Counter(), 'z': Counter()}

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(None)