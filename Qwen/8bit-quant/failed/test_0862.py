import pytest
from src_0862 import task_func
from collections import Counter

def test_task_func_with_empty_input():
    assert task_func([]) == []

def test_task_func_with_single_empty_list():
    assert task_func([[]]) == [Counter()]

def test_task_func_with_single_list():
    result = task_func([[1, 2]])
    assert len(result) == 1
    assert isinstance(result[0], Counter)
    assert sum(result[0].values()) == 2
    assert all(item in POSSIBLE_ITEMS for item in result[0])

def test_task_func_with_multiple_lists():
    result = task_func([[1, 2], [3, 4, 5]])
    assert len(result) == 2
    assert isinstance(result[0], Counter)
    assert isinstance(result[1], Counter)
    assert sum(result[0].values()) == 2
    assert sum(result[1].values()) == 3
    assert all(item in POSSIBLE_ITEMS for item in result[0])
    assert all(item in POSSIBLE_ITEMS for item in result[1])

def test_task_func_with_reproducibility():
    result1 = task_func([[1, 2], [3, 4, 5]])
    result2 = task_func([[1, 2], [3, 4, 5]])
    assert result1 == result2