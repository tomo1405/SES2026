import pytest
from src_0792 import task_func
from collections import Counter
from itertools import cycle

def test_task_func_empty_list():
    assert task_func([]) == Counter()

def test_task_func_single_element():
    result = task_func(['A'])
    assert len(result) == 1
    assert 'A' in result
    assert result['A'] == 30

def test_task_func_multiple_elements():
    result = task_func(['A', 'B', 'C'])
    assert len(result) == 3
    assert all(element in result for element in ['A', 'B', 'C'])
    assert sum(result.values()) == 30

def test_task_func_all_same_elements():
    result = task_func(['A', 'A', 'A', 'A', 'A'])
    assert len(result) == 1
    assert 'A' in result
    assert result['A'] == 30

def test_task_func_unique_elements():
    result = task_func(list('ABCDEFGHIJ'))
    assert len(result) == 10
    assert all(element in result for element in 'ABCDEFGHIJ')
    assert sum(result.values()) == 30

def test_task_func_random_elements():
    elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    random.shuffle(elements)
    result = task_func(elements)
    assert len(result) == 10
    assert all(element in result for element in elements)
    assert sum(result.values()) == 30

def test_task_func_rotation():
    result = task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    keys = list(result.keys())
    rotated_keys = keys[3:] + keys[:3]
    rotated_result = Counter({k: result[k] for k in rotated_keys})
    assert rotated_result == result