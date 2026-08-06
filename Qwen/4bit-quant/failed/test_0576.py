import pytest
from src_0576 import task_func
import pandas as pd
import numpy as np

def test_task_func_empty_list():
    result = task_func([])
    assert result.empty

def test_task_func_single_element():
    result = task_func([1])
    assert result.equals(pd.DataFrame({0: [1], 1: [np.nan], 2: [np.nan], 3: [np.nan], 4: [np.nan]}))

def test_task_func_multiple_elements():
    result = task_func([1, 2, 3, 4, 5])
    assert result.shape == (5, 5)

def test_task_func_n_groups():
    result = task_func([1, 2, 3], n_groups=3)
    assert result.shape == (3, 3)

def test_task_func_shuffling():
    result = task_func([1, 2, 3, 4, 5])
    assert not all(result.iloc[0] == [1, 2, 3, 4, 5])

def test_task_func_rolling():
    result = task_func([1, 2, 3, 4, 5])
    assert result.iloc[0].isnull().all()
    assert result.iloc[-1].equals(pd.Series([1, 2, 3, 4, 5]))

def test_task_func_with_zeros():
    result = task_func([0, 0, 0, 0, 0])
    assert result.equals(pd.DataFrame(np.zeros((5, 5))))

def test_task_func_with_negative_numbers():
    result = task_func([-1, -2, -3, -4, -5])
    assert result.shape == (5, 5)