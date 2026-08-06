import pytest
from src_0336 import task_func
from collections import OrderedDict

def test_task_func_default_length():
    result = task_func()
    assert isinstance(result, OrderedDict)
    assert len(result) <= 5  # Since there are only 5 letters

def test_task_func_custom_length():
    length = 200
    result = task_func(length)
    assert isinstance(result, OrderedDict)
    assert len(result) <= 5

def test_task_func_letter_counts():
    result = task_func(1000)
    for letter, count in result.items():
        assert letter in 'abcde'
        assert isinstance(count, int)
        assert count > 0

def test_task_func_order():
    result = task_func(1000)
    counts = list(result.values())
    assert counts == sorted(counts, reverse=True)

def test_task_func_empty_string():
    result = task_func(0)
    assert result == OrderedDict()

def test_task_func_single_letter():
    result = task_func(1)
    assert len(result) == 1
    assert next(iter(result.values())) == 1