import pytest
from src_0903 import task_func

def test_task_func():
    d = {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5], 'z': [1, 2, 3, 4, 5]}
    counts = task_func(d)
    assert counts['x'] == Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2})
    assert counts['y'] == Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2})
    assert counts['z'] == Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2})

def test_task_func_with_missing_column():
    d = {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5]}
    counts = task_func(d)
    assert counts['x'] == Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2})
    assert counts['y'] == Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2})
    assert counts['z'] == Counter()

def test_task_func_with_empty_column():
    d = {'x': [], 'y': [], 'z': []}
    counts = task_func(d)
    assert counts['x'] == Counter()
    assert counts['y'] == Counter()
    assert counts['z'] == Counter()

def test_task_func_with_invalid_input():
    d = {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5], 'z': [1, 2, 3, 4, 5], 'a': [1, 2, 3, 4, 5]}
    with pytest.raises(KeyError):
        task_func(d)