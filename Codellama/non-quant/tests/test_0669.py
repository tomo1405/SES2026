import pytest
from src_0669 import task_func

def test_task_func():
    x = [('a', 1), ('b', 2), ('c', 3)]
    expected_result = ['a', 'b', 'c']
    assert task_func(x) == expected_result

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    expected_result = ['a', 'b', 'c', 'd']
    assert task_func(x) == expected_result

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
    expected_result = ['a', 'b', 'c', 'd', 'e']
    assert task_func(x) == expected_result

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
    expected_result = ['a', 'b', 'c', 'd', 'e', 'f']
    assert task_func(x) == expected_result

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7)]
    expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert task_func(x) == expected_result

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8)]
    expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    assert task_func(x) == expected_result

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9)]
    expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    assert task_func(x) == expected_result

    x = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10)]
    expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    assert task_func(x) == expected_result