import pytest
from src_0024 import task_func

def test_task_func_with_equal_lists():
    l1 = [0.3, 0.6, 0.9]
    l2 = [0.4, 0.7, 1.0]
    assert task_func(l1, l2) == 0.6

def test_task_func_with_one_empty_list():
    l1 = []
    l2 = [0.4, 0.7, 1.0]
    assert task_func(l1, l2) == 0.4

def test_task_func_with_threshold():
    l1 = [0.1, 0.2, 0.3]
    l2 = [0.4, 0.5, 0.6]
    assert task_func(l1, l2, THRESHOLD=0.3) == 0.3

def test_task_func_with_large_threshold():
    l1 = [0.1, 0.2, 0.3]
    l2 = [0.4, 0.5, 0.6]
    assert task_func(l1, l2, THRESHOLD=0.8) == 0.6

def test_task_func_with_negative_values():
    l1 = [-0.5, -0.2, 0.1]
    l2 = [-0.6, -0.3, 0.2]
    assert task_func(l1, l2) == -0.2

def test_task_func_with_mixed_types():
    l1 = [0.1, 0.2, 0.3]
    l2 = [0.4, 0.7, 'a']
    with pytest.raises(TypeError):
        task_func(l1, l2)

def test_task_func_with_non_numeric_values():
    l1 = ['a', 'b', 'c']
    l2 = ['d', 'e', 'f']
    with pytest.raises(TypeError):
        task_func(l1, l2)