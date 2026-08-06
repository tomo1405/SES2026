import pytest
from src_0458 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_input():
    L = [[1, 2, 3], [4, 5], [6]]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)
    assert ax.dtype == np.int64

def test_task_func_empty_sublists():
    L = [[], [1, 2], [], [3]]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)
    assert ax.dtype == np.int64

def test_task_func_single_element_lists():
    L = [[1], [2], [3]]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)
    assert ax.dtype == np.int64

def test_task_func_non_integer_elements():
    L = [[1, 2, 'a'], [4, 5]]
    with pytest.raises(TypeError, match="Expected list of list of int"):
        task_func(L)

def test_task_func_empty_list():
    L = []
    with pytest.raises(TypeError, match="Expected list of list of int"):
        task_func(L)

def test_task_func_mixed_data_types():
    L = [[1, 2], [3.0, 4], [5]]
    with pytest.raises(TypeError, match="Expected list of list of int"):
        task_func(L)