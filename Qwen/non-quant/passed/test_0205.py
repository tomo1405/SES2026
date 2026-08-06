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
    expected_std_dev = np.std(L)
    assert np.isclose(result['std_dev'], expected_std_dev)

def test_task_func_plot():
    L = [1, 2, 3, 4, 5]
    result = task_func(L)
    assert isinstance(result['plot'], plt.Axes)