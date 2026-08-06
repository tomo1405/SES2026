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
    assert sum(result.values()) == 30

def test_task_func_all_elements():
    result = task_func(ELEMENTS)
    assert len(result) == 10
    assert sum(result.values()) == 30

def test_task_func_repeated_elements():
    result = task_func(['A', 'A', 'A', 'B', 'B', 'B'])
    assert len(result) == 2
    assert sum(result.values()) == 30

def test_task_func_random_elements():
    random_elements = random.sample(ELEMENTS, 5)
    result = task_func(random_elements)
    assert len(result) == 5
    assert sum(result.values()) == 30

def test_task_func_cycle_shift():
    result = task_func(['A', 'B', 'C', 'D', 'E'])
    keys = list(result.keys())
    assert keys[3:] + keys[:3] == list(result.keys())