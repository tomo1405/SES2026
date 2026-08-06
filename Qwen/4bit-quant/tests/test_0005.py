import pytest
from src_0005 import task_func

def test_task_func_with_empty_dict():
    assert task_func({}) == {}

def test_task_func_with_single_list():
    assert task_func({'a': [1, 2, 3]}) == {1: 1, 2: 1, 3: 1}

def test_task_func_with_multiple_lists():
    assert task_func({'a': [1, 2], 'b': [2, 3], 'c': [3, 4]}) == {1: 1, 2: 2, 3: 2, 4: 1}

def test_task_func_with_nested_lists():
    assert task_func({'a': [[1, 2], [2, 3]], 'b': [3, 4]}) == {1: 1, 2: 2, 3: 2, 4: 1}

def test_task_func_with_mixed_data_types():
    assert task_func({'a': [1, 'a'], 'b': ['a', 2, 2]}) == {1: 1, 'a': 2, 2: 2}

def test_task_func_with_duplicates_in_same_key():
    assert task_func({'a': [1, 1, 1], 'b': [1]}) == {1: 4}

def test_task_func_with_empty_lists():
    assert task_func({'a': [], 'b': [], 'c': []}) == {}