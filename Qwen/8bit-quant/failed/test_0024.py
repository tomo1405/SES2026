import pytest
from src_0024 import task_func

def test_task_func_with_equal_lengths():
    l1 = [0.1, 0.2, 0.3]
    l2 = [0.4, 0.5, 0.6]
    assert task_func(l1, l2) == 0.5

def test_task_func_with_l1_shorter():
    l1 = [0.1, 0.2]
    l2 = [0.4, 0.5, 0.6]
    assert task_func(l1, l2) == 0.5

def test_task_func_with_l2_shorter():
    l1 = [0.1, 0.2, 0.3]
    l2 = [0.4, 0.5]
    assert task_func(l1, l2) == 0.5

def test_task_func_with_all_elements_above_threshold():
    l1 = [0.6, 0.7, 0.8]
    l2 = [0.9, 1.0, 1.1]
    assert task_func(l1, l2) == 0.9

def test_task_func_with_all_elements_below_threshold():
    l1 = [0.0, 0.1, 0.2]
    l2 = [0.3, 0.4, 0.5]
    assert task_func(l1, l2) == 0.4

def test_task_func_with_single_element_lists():
    l1 = [0.3]
    l2 = [0.7]
    assert task_func(l1, l2) == 0.7

def test_task_func_with_empty_lists():
    l1 = []
    l2 = []
    with pytest.raises(IndexError):
        task_func(l1, l2)

def test_task_func_with_one_empty_list():
    l1 = []
    l2 = [0.5]
    assert task_func(l1, l2) == 0.5

def test_task_func_with_custom_threshold():
    l1 = [0.1, 0.2, 0.3]
    l2 = [0.4, 0.5, 0.6]
    assert task_func(l1, l2, THRESHOLD=0.3) == 0.4

def test_task_func_with_negative_numbers():
    l1 = [-0.1, -0.2, -0.3]
    l2 = [-0.4, -0.5, -0.6]
    assert task_func(l1, l2) == -0.5