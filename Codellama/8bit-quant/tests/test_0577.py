import pandas as pd
from src_0577 import task_func


def test_task_func_empty_list():
    assert task_func([]) == pd.Series()

def test_task_func_single_element_list():
    assert task_func([1]) == pd.Series([1])

def test_task_func_multiple_element_list():
    l = [1, 2, 3, 4, 5]
    n_groups = 3
    expected_result = pd.Series([1, 2, 3, 4, 5])
    assert task_func(l, n_groups) == expected_result

def test_task_func_random_shifts():
    l = [1, 2, 3, 4, 5]
    n_groups = 3
    expected_result = pd.Series([1, 2, 3, 4, 5])
    assert task_func(l, n_groups) == expected_result

def test_task_func_random_shifts_with_empty_list():
    l = []
    n_groups = 3
    expected_result = pd.Series()
    assert task_func(l, n_groups) == expected_result

def test_task_func_random_shifts_with_single_element_list():
    l = [1]
    n_groups = 3
    expected_result = pd.Series([1])
    assert task_func(l, n_groups) == expected_result

def test_task_func_random_shifts_with_multiple_element_list():
    l = [1, 2, 3, 4, 5]
    n_groups = 3
    expected_result = pd.Series([1, 2, 3, 4, 5])
    assert task_func(l, n_groups) == expected_result