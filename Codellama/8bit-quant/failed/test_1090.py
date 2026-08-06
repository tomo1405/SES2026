import pytest
from src_1090 import task_func

def test_task_func():
    list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    total_sum, category_counts = task_func(list_of_tuples)
    assert total_sum == 6
    assert category_counts == {'a': 1, 'b': 1, 'c': 1}

def test_task_func_empty_list():
    list_of_tuples = []
    total_sum, category_counts = task_func(list_of_tuples)
    assert total_sum == 0
    assert category_counts == {}

def test_task_func_invalid_input():
    list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    with pytest.raises(ValueError):
        task_func(list_of_tuples)