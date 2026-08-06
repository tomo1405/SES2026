import pytest
from src_0205 import task_func
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def test_task_func_mean():
    L = [1, 2, 3, 4, 5]
    result = task_func(L)
    assert np.isclose(result['mean'], 3.0)

def test_task_func_median():
    L = [1, 2, 3, 4, 5]
    result = task_func(L)
    assert np.isclose(result['median'], 3.0)

def test_task_func_mode():
    L = [1, 2, 2, 3, 4]
    result = task_func(L)
    assert result['mode'] == 2

def test_task_func_std_dev():
    L = [1, 2, 3, 4, 5]
    result = task_func(L)
    assert np.isclose(result['std_dev'], np.std(L))

def test_task_func_plot():
    L = [1, 2, 3, 4, 5]
    result = task_func(L)
    assert isinstance(result['plot'], plt.Axes)

def test_task_func_empty_list():
    L = []
    with pytest.raises(IndexError):
        task_func(L)

def test_task_func_single_element():
    L = [42]
    result = task_func(L)
    assert np.isclose(result['mean'], 42.0)
    assert np.isclose(result['median'], 42.0)
    assert result['mode'] == 42
    assert np.isclose(result['std_dev'], 0.0)
    assert isinstance(result['plot'], plt.Axes)