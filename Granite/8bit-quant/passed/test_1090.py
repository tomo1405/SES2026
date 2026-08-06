import pytest
from src_1090 import task_func

list_of_tuples = [(1, 'A'), (2, 'B'), (3, 'A'), (4, 'C'), (5, 'B')]

def test_task_func():
    total_sum, category_counts = task_func(list_of_tuples)
    assert total_sum == 15
    assert category_counts == {'A': 2, 'B': 2, 'C': 1}

def test_task_func_empty_list():
    total_sum, category_counts = task_func([])
    assert total_sum == 0
    assert category_counts == {}

def test_task_func_single_tuple():
    total_sum, category_counts = task_func([(10, 'X')])
    assert total_sum == 10
    assert category_counts == {'X': 1}

def test_task_func_negative_values():
    list_of_tuples = [(1, 'A'), (-2, 'B'), (3, 'A'), (-4, 'C'), (5, 'B')]
    total_sum, category_counts = task_func(list_of_tuples)
    assert total_sum == 0
    assert category_counts == {'A': 2, 'B': 2, 'C': 1}