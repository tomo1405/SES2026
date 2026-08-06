import pytest
from src_0792 import task_func
from collections import Counter

def test_task_func_empty_list():
    assert task_func([]) == Counter()

def test_task_func_single_element():
    result = task_func(['A'])
    assert len(result) == 1
    assert result['A'] == 30

def test_task_func_multiple_elements():
    result = task_func(['A', 'B', 'C'])
    assert len(result) == 3
    assert all(value == 10 for value in result.values())

def test_task_func_all_same_elements():
    result = task_func(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'])
    assert len(result) == 1
    assert result['A'] == 30

def test_task_func_random_elements():
    elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    result = task_func(elements * 3)
    assert len(result) == 10
    assert sum(result.values()) == 30

def test_task_func_rotation():
    elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    result = task_func(elements)
    keys = list(result.keys())
    rotated_keys = keys[3:] + keys[:3]
    assert list(result.keys()) == rotated_keys

def test_task_func_preserves_counts():
    elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    result = task_func(elements * 3)
    assert all(result[key] == 3 for key in result)