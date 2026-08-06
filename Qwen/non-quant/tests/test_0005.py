import pytest
from src_0005 import task_func

def test_task_func_empty_dict():
    assert task_func({}) == {}

def test_task_func_single_value():
    assert task_func({'a': [1]}) == {1: 1}

def test_task_func_multiple_values():
    assert task_func({'a': [1, 2], 'b': [2, 3]}) == {1: 1, 2: 2, 3: 1}

def test_task_func_with_duplicates():
    assert task_func({'a': [1, 1, 2], 'b': [2, 2, 3]}) == {1: 2, 2: 3, 3: 1}

def test_task_func_with_nested_lists():
    assert task_func({'a': [[1, 2], [3]], 'b': [[2, 3], [4]]}) == {1: 1, 2: 2, 3: 2, 4: 1}

def test_task_func_with_empty_lists():
    assert task_func({'a': [], 'b': []}) == {}

def test_task_func_with_mixed_data_types():
    assert task_func({'a': [1, 'a'], 'b': ['a', 2]}) == {1: 1, 'a': 2, 2: 1}