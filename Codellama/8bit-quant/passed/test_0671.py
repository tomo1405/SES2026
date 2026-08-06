import pytest
from src_0671 import task_func

def test_task_func_1():
    x = 'abc'
    w = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(x, w) == 'abc'

def test_task_func_2():
    x = 'abcd'
    w = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert task_func(x, w) == 'abcd'

def test_task_func_3():
    x = 'abcde'
    w = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    assert task_func(x, w) == 'abcde'

def test_task_func_4():
    x = 'abcdef'
    w = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    assert task_func(x, w) == 'abcdef'

def test_task_func_5():
    x = 'abcdefg'
    w = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
    assert task_func(x, w) == 'abcdefg'