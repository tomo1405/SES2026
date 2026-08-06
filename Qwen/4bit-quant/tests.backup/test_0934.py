import pytest
from src_0934 import task_func

def test_task_func_single_letter():
    result = task_func('a')
    expected_tuples = [('a', 1)]
    expected_split = ['a']
    assert result[0] == expected_tuples
    assert result[1] == expected_split

def test_task_func_multiple_letters():
    result = task_func('abc')
    expected_tuples = [('a', 1), ('b', 2), ('c', 3)]
    expected_split = ['abc']
    assert result[0] == expected_tuples
    assert result[1] == expected_split

def test_task_func_with_wordninja_split():
    result = task_func('hellothere')
    expected_tuples = [('h', 8), ('e', 5), ('l', 12), ('l', 12), ('o', 15), ('t', 20), ('h', 8), ('e', 5), ('r', 18), ('e', 5)]
    expected_split = ['hello', 'there']
    assert result[0] == expected_tuples
    assert result[1] == expected_split

def test_task_func_uppercase():
    result = task_func('ABC')
    expected_tuples = [('A', 1), ('B', 2), ('C', 3)]
    expected_split = ['abc']
    assert result[0] == expected_tuples
    assert result[1] == expected_split

def test_task_func_empty_string():
    result = task_func('')
    expected_tuples = []
    expected_split = []
    assert result[0] == expected_tuples
    assert result[1] == expected_split

def test_task_func_special_characters():
    result = task_func('!@#')
    expected_tuples = []
    expected_split = []
    assert result[0] == expected_tuples
    assert result[1] == expected_split