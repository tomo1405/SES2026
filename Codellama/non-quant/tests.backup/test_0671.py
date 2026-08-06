import pytest
from src_0671 import task_func

def test_task_func():
    x = 'abc'
    w = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(x, w) == 'abc'

def test_task_func_empty_string():
    x = ''
    w = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(x, w) == ''

def test_task_func_empty_dict():
    x = 'abc'
    w = {}
    assert task_func(x, w) == ''

def test_task_func_invalid_input():
    x = 'abc'
    w = {'a': 1, 'b': 2, 'c': 3}
    with pytest.raises(ValueError):
        task_func(x, w, invalid_input=True)