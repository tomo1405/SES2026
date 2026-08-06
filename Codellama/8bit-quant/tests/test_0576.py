import pandas as pd
from src_0576 import task_func


def test_task_func_empty_list():
    assert task_func([]) == pd.DataFrame()

def test_task_func_non_empty_list():
    l = [1, 2, 3, 4, 5]
    n_groups = 3
    expected_output = pd.DataFrame([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    assert task_func(l, n_groups) == expected_output

def test_task_func_non_empty_list_with_n_groups_1():
    l = [1, 2, 3, 4, 5]
    n_groups = 1
    expected_output = pd.DataFrame([[1], [2], [3], [4], [5]])
    assert task_func(l, n_groups) == expected_output

def test_task_func_non_empty_list_with_n_groups_2():
    l = [1, 2, 3, 4, 5]
    n_groups = 2
    expected_output = pd.DataFrame([[1, 2], [2, 3], [3, 4], [4, 5]])
    assert task_func(l, n_groups) == expected_output

def test_task_func_non_empty_list_with_n_groups_3():
    l = [1, 2, 3, 4, 5]
    n_groups = 3
    expected_output = pd.DataFrame([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    assert task_func(l, n_groups) == expected_output

def test_task_func_non_empty_list_with_n_groups_4():
    l = [1, 2, 3, 4, 5]
    n_groups = 4
    expected_output = pd.DataFrame([[1, 2, 3, 4], [2, 3, 4, 5]])
    assert task_func(l, n_groups) == expected_output

def test_task_func_non_empty_list_with_n_groups_5():
    l = [1, 2, 3, 4, 5]
    n_groups = 5
    expected_output = pd.DataFrame([[1, 2, 3, 4, 5]])
    assert task_func(l, n_groups) == expected_output