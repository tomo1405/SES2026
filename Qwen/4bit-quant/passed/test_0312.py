import pytest
from src_0312 import task_func

def test_task_func_with_non_empty_lists():
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    result = task_func(list_of_lists)
    assert result['mean'] == 3.5
    assert result['median'] == 3.5
    assert result['mode'] == 3

def test_task_func_with_empty_lists():
    list_of_lists = [[], []]
    result = task_func(list_of_lists)
    assert result['mean'] == 50.0
    assert result['median'] == 50.0
    assert result['mode'] == 50

def test_task_func_with_mixed_lists():
    list_of_lists = [[1, 2, 3], [], [7, 8, 9]]
    result = task_func(list_of_lists)
    assert result['mean'] == 5.0
    assert result['median'] == 5.0
    assert result['mode'] == 1

def test_task_func_with_single_element_lists():
    list_of_lists = [[1], [2], [3]]
    result = task_func(list_of_lists)
    assert result['mean'] == 2.0
    assert result['median'] == 2.0
    assert result['mode'] == 1

def test_task_func_with_large_numbers():
    list_of_lists = [[1000, 2000, 3000], [4000, 5000, 6000]]
    result = task_func(list_of_lists)
    assert result['mean'] == 3500.0
    assert result['median'] == 3500.0
    assert result['mode'] == 1000

def test_task_func_with_custom_size():
    list_of_lists = [[], []]
    result = task_func(list_of_lists, size=10)
    assert result['mean'] == 50.0
    assert result['median'] == 50.0
    assert result['mode'] == 50

def test_task_func_with_custom_seed():
    list_of_lists = [[], []]
    result = task_func(list_of_lists, seed=42)
    assert result['mean'] == 50.0
    assert result['median'] == 50.0
    assert result['mode'] == 50