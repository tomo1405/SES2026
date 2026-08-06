import pytest
from src_0343 import task_func

def test_task_func_with_no_match():
    elements = ['abc', 'def']
    pattern = 'xyz'
    result = task_func(elements, pattern)
    assert isinstance(result[0], list)
    assert all(isinstance(item, str) and item.startswith('%') and item.endswith('%') for item in result[0])
    assert len(result[0]) == 2
    assert not result[1]

def test_task_func_with_match():
    elements = ['abc', 'def']
    pattern = 'a'
    result = task_func(elements, pattern)
    assert isinstance(result[0], list)
    assert all(isinstance(item, str) and item.startswith('%') and item.endswith('%') for item in result[0])
    assert len(result[0]) == 2
    assert result[1]

def test_task_func_with_empty_elements():
    elements = []
    pattern = 'a'
    result = task_func(elements, pattern)
    assert isinstance(result[0], list)
    assert not result[0]
    assert not result[1]

def test_task_func_with_empty_pattern():
    elements = ['abc', 'def']
    pattern = ''
    result = task_func(elements, pattern)
    assert isinstance(result[0], list)
    assert all(isinstance(item, str) and item.startswith('%') and item.endswith('%') for item in result[0])
    assert len(result[0]) == 2
    assert result[1]

def test_task_func_with_seed():
    elements = ['abc', 'def']
    pattern = 'a'
    result1 = task_func(elements, pattern, seed=100)
    result2 = task_func(elements, pattern, seed=100)
    assert result1 == result2

def test_task_func_with_different_seed():
    elements = ['abc', 'def']
    pattern = 'a'
    result1 = task_func(elements, pattern, seed=100)
    result2 = task_func(elements, pattern, seed=200)
    assert result1 != result2