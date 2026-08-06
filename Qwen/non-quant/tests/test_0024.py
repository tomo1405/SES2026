import pytest
from src_0024 import task_func

def test_task_func_equal_lists():
    l1 = [0.3, 0.7, 0.9]
    l2 = [0.3, 0.7, 0.9]
    assert task_func(l1, l2) == 0.7

def test_task_func_different_lengths():
    l1 = [0.1, 0.2, 0.3]
    l2 = [0.8, 0.9]
    assert task_func(l1, l2) == 0.8

def test_task_func_one_empty_list():
    l1 = []
    l2 = [0.4, 0.6, 0.8]
    assert task_func(l1, l2) == 0.6

def test_task_func_both_empty_lists():
    l1 = []
    l2 = []
    with pytest.raises(IndexError):
        task_func(l1, l2)

def test_task_func_threshold_zero():
    l1 = [-0.5, 0.5, 1.5]
    l2 = [-1.5, 0.5, 2.5]
    assert task_func(l1, l2, THRESHOLD=0.0) == 0.5

def test_task_func_threshold_one():
    l1 = [0.1, 0.9, 1.9]
    l2 = [0.2, 0.8, 1.8]
    assert task_func(l1, l2, THRESHOLD=1.0) == 1.9

def test_task_func_negative_values():
    l1 = [-0.7, -0.3, -0.1]
    l2 = [-0.8, -0.4, -0.2]
    assert task_func(l1, l2) == -0.3