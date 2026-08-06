import pytest
from src_1090 import task_func

def test_task_func_with_empty_list():
    result = task_func([])
    assert result == (0, {})

def test_task_func_with_single_tuple():
    result = task_func([(5, 'a')])
    assert result == (5, {'a': 1})

def test_task_func_with_multiple_tuples_same_category():
    result = task_func([(1, 'a'), (2, 'a'), (3, 'a')])
    assert result == (6, {'a': 3})

def test_task_func_with_multiple_tuples_different_categories():
    result = task_func([(1, 'a'), (2, 'b'), (3, 'a')])
    assert result == (6, {'a': 2, 'b': 1})

def test_task_func_with_negative_numbers():
    result = task_func([(-1, 'a'), (-2, 'b'), (3, 'a')])
    assert result == (0, {'a': 2, 'b': 1})

def test_task_func_with_mixed_types():
    with pytest.raises(TypeError):
        task_func([(1, 'a'), ('two', 'b'), (3, 'a')])

def test_task_func_with_large_numbers():
    result = task_func([(10**6, 'a'), (10**6, 'b'), (10**6, 'a')])
    assert result == (3 * 10**6, {'a': 2, 'b': 1})