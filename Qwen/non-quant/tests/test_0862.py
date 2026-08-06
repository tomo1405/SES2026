from collections import Counter

import pytest
from src_0862 import task_func


def test_task_func_with_empty_list():
    assert task_func([]) == []

def test_task_func_with_single_empty_list():
    assert task_func([[]]) == [Counter()]

def test_task_func_with_single_list():
    result = task_func([[1]])
    assert len(result) == 1
    assert isinstance(result[0], Counter)
    assert sum(result[0].values()) == 1

def test_task_func_with_multiple_lists():
    result = task_func([[1], [2], [3]])
    assert len(result) == 3
    for basket in result:
        assert isinstance(basket, Counter)
        assert sum(basket.values()) == 1

def test_task_func_with_reproducibility():
    result1 = task_func([[1, 2, 3]])
    result2 = task_func([[1, 2, 3]])
    assert result1 == result2

def test_task_func_with_large_input():
    result = task_func([[1] * 100])
    assert len(result) == 1
    assert isinstance(result[0], Counter)
    assert sum(result[0].values()) == 100

def test_task_func_with_various_lengths():
    result = task_func([[1], [2, 3], [4, 5, 6]])
    assert len(result) == 3
    for i, basket in enumerate(result):
        assert isinstance(basket, Counter)
        assert sum(basket.values()) == len(list_of_lists[i])

def test_task_func_with_no_possible_items():
    original_possible_items = task_func.POSSIBLE_ITEMS
    task_func.POSSIBLE_ITEMS = []
    with pytest.raises(IndexError):
        task_func([[1]])
    task_func.POSSIBLE_ITEMS = original_possible_items