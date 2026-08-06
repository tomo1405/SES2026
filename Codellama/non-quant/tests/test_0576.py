import pandas as pd
from src_0576 import task_func


def test_task_func_empty_list():
    l = []
    n_groups = 5
    expected = pd.DataFrame()
    assert task_func(l, n_groups) == expected

def test_task_func_non_empty_list():
    l = [1, 2, 3, 4, 5]
    n_groups = 5
    expected = pd.DataFrame([[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]])
    assert task_func(l, n_groups) == expected

def test_task_func_n_groups_1():
    l = [1, 2, 3, 4, 5]
    n_groups = 1
    expected = pd.DataFrame([[1, 2, 3, 4, 5]])
    assert task_func(l, n_groups) == expected

def test_task_func_n_groups_2():
    l = [1, 2, 3, 4, 5]
    n_groups = 2
    expected = pd.DataFrame([[1, 2, 3, 4, 5], [2, 3, 4, 5, 1]])
    assert task_func(l, n_groups) == expected

def test_task_func_n_groups_3():
    l = [1, 2, 3, 4, 5]
    n_groups = 3
    expected = pd.DataFrame([[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2]])
    assert task_func(l, n_groups) == expected

def test_task_func_n_groups_4():
    l = [1, 2, 3, 4, 5]
    n_groups = 4
    expected = pd.DataFrame([[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3]])
    assert task_func(l, n_groups) == expected

def test_task_func_n_groups_5():
    l = [1, 2, 3, 4, 5]
    n_groups = 5
    expected = pd.DataFrame([[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]])
    assert task_func(l, n_groups) == expected