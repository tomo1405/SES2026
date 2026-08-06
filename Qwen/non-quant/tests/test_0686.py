import pytest
from src_0686 import task_func
from collections import Counter

def test_task_func_with_empty_lists():
    assert task_func([[], []]) == Counter()

def test_task_func_with_single_list():
    assert task_func([[1, 2, 3]]) == Counter({1: 1, 2: 1, 3: 1})

def test_task_func_with_multiple_lists():
    assert task_func([[1, 2], [2, 3], [3, 4]]) == Counter({1: 1, 2: 2, 3: 2, 4: 1})

def test_task_func_with_duplicates_in_single_list():
    assert task_func([[1, 1, 2, 2]]) == Counter({1: 2, 2: 2})

def test_task_func_with_mixed_data_types():
    assert task_func([[1, 'a'], ['a', 2], [2, 1]]) == Counter({1: 2, 'a': 2, 2: 2})

def test_task_func_with_nested_lists():
    with pytest.raises(TypeError):
        task_func([[[1, 2], 3], [4, 5]])