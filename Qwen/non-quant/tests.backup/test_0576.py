import pytest
from src_0576 import task_func
import pandas as pd
import numpy as np

def test_task_func_empty_list():
    result = task_func([])
    assert result.empty

def test_task_func_single_element():
    result = task_func([1])
    assert result.equals(pd.DataFrame([[1]]))

def test_task_func_multiple_elements_default_groups():
    l = [1, 2, 3]
    result = task_func(l)
    assert result.shape == (5, 3)
    assert all(result.iloc[0] == np.roll(l, -5))

def test_task_func_multiple_elements_custom_groups():
    l = [1, 2, 3, 4, 5]
    n_groups = 3
    result = task_func(l, n_groups=n_groups)
    assert result.shape == (n_groups, len(l))
    assert all(result.iloc[0] == np.roll(l, -n_groups))

def test_task_func_large_list():
    l = list(range(100))
    result = task_func(l)
    assert result.shape == (5, 100)
    assert all(result.iloc[0] == np.roll(l, -5))

def test_task_func_non_numeric_elements():
    l = ['a', 'b', 'c']
    result = task_func(l)
    assert result.shape == (5, 3)
    assert all(result.iloc[0] == np.roll(l, -5))

def test_task_func_mixed_elements():
    l = [1, 'a', 3.14]
    result = task_func(l)
    assert result.shape == (5, 3)
    assert all(result.iloc[0] == np.roll(l, -5))