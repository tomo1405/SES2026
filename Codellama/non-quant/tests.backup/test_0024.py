import pytest
from src_0024 import task_func

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5, 6]
    THRESHOLD = 0.5
    expected_result = 2
    assert task_func(l1, l2, THRESHOLD) == expected_result

def test_task_func_with_different_threshold():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5, 6]
    THRESHOLD = 0.7
    expected_result = 3
    assert task_func(l1, l2, THRESHOLD) == expected_result

def test_task_func_with_unequal_length_lists():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5]
    THRESHOLD = 0.5
    expected_result = 2
    assert task_func(l1, l2, THRESHOLD) == expected_result

def test_task_func_with_empty_lists():
    l1 = []
    l2 = []
    THRESHOLD = 0.5
    expected_result = None
    assert task_func(l1, l2, THRESHOLD) == expected_result

def test_task_func_with_one_empty_list():
    l1 = [1, 2, 3, 4, 5]
    l2 = []
    THRESHOLD = 0.5
    expected_result = None
    assert task_func(l1, l2, THRESHOLD) == expected_result