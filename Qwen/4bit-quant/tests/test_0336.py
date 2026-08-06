import pytest
from src_0336 import task_func
import collections
from queue import PriorityQueue

def test_task_func_default_length():
    result = task_func()
    assert isinstance(result, collections.OrderedDict)
    assert len(result) <= len(task_func.LETTERS)

def test_task_func_custom_length():
    length = 50
    result = task_func(length)
    assert isinstance(result, collections.OrderedDict)
    assert len(result) <= len(task_func.LETTERS)
    assert sum(result.values()) == length

def test_task_func_empty_string():
    with pytest.raises(ValueError):
        task_func(string_length=0)

def test_task_func_single_letter():
    result = task_func(string_length=1)
    assert isinstance(result, collections.OrderedDict)
    assert len(result) == 1

def test_task_func_all_same_letters():
    result = task_func(string_length=100, LETTERS=['a'])
    assert isinstance(result, collections.OrderedDict)
    assert len(result) == 1
    assert result['a'] == 100

def test_task_func_pq_order():
    result = task_func()
    prev_count = float('inf')
    for count in result.values():
        assert count <= prev_count
        prev_count = count