import pytest
from src_0576 import task_func
import pandas as pd
import numpy as np

def test_task_func_empty_list():
    result = task_func([])
    assert result.empty

def test_task_func_single_element():
    result = task_func([1])
    assert result.shape == (5, 1)
    assert result.iloc[0, 0] == 1

def test_task_func_multiple_elements():
    l = [1, 2, 3, 4, 5]
    result = task_func(l)
    assert result.shape == (5, 5)
    assert result.iloc[:, 0].unique().size == len(l)  # Check if all elements are present

def test_task_func_n_groups():
    l = [1, 2, 3, 4, 5]
    n_groups = 3
    result = task_func(l, n_groups)
    assert result.shape == (3, 5)

def test_task_func_rolling_shift():
    l = [1, 2, 3, 4, 5]
    result = task_func(l)
    first_row = result.iloc[0]
    last_row = result.iloc[-1]
    assert (first_row == np.roll(last_row, -len(l))).all()

def test_task_func_randomness():
    l = [1, 2, 3, 4, 5]
    result1 = task_func(l)
    result2 = task_func(l)
    assert not result1.equals(result2)  # Check if shuffling is different each time