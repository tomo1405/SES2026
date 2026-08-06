import pytest
from src_0669 import task_func

def test_task_func():
    x = [('a', 1), ('b', 2), ('c', 3)]
    expected = ['a', 'b', 'c']
    assert task_func(x) == expected

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    expected = ['a', 'b', 'c', 'd']
    assert task_func(x) == expected

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
    expected = ['a', 'b', 'c', 'd', 'e']
    assert task_func(x) == expected

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    assert task_func(x) == expected