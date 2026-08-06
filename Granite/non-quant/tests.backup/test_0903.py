import pytest
from src_0903 import task_func

def test_task_func():
    d = {'x': [1, 2, 3], 'y': [4, 5, 6], 'z': [7, 8, 9]}
    expected_output = {'x': Counter({1: 1, 2: 1, 3: 1}),
                       'y': Counter({4: 1, 5: 1, 6: 1}),
                       'z': Counter({7: 1, 8: 1, 9: 1})}
    actual_output = task_func(d)
    assert actual_output == expected_output

def test_task_func_with_missing_key():
    d = {'x': [1, 2, 3], 'y': [4, 5, 6]}
    expected_output = {'x': Counter({1: 1, 2: 1, 3: 1}),
                       'y': Counter({4: 1, 5: 1, 6: 1}),
                       'z': Counter()}
    actual_output = task_func(d)
    assert actual_output == expected_output

def test_task_func_with_empty_dict():
    d = {}
    expected_output = {'x': Counter(),
                       'y': Counter(),
                       'z': Counter()}
    actual_output = task_func(d)
    assert actual_output == expected_output