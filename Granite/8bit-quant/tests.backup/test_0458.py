import pandas as pd
import numpy as np
from src_0458 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)

def test_task_func_with_floats():
    L = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    try:
        task_func(L)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError not raised"

def test_task_func_with_non_integer_values():
    L = [[1, 2, 3], [4, 5, 6.5], [7, 8, 9]]
    try:
        task_func(L)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError not raised"

def test_task_func_with_empty_lists():
    L = [[], [], []]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)

def test_task_func_with_nested_lists():
    L = [[1, 2, 3], [4, 5, [6, 7]], [7, 8, 9]]
    try:
        task_func(L)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError not raised"