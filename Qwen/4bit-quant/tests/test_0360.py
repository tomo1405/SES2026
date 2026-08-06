import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0360 import task_func


def test_task_func_with_positive_correlation():
    data_dict = {
        'A': [1, 2, 3, 4, 5],
        'B': [2, 4, 6, 8, 10]
    }
    data_keys = ['A', 'B']
    correlation, ax = task_func(data_dict, data_keys)
    assert np.isclose(correlation, 1.0)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_negative_correlation():
    data_dict = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 8, 6, 4, 2]
    }
    data_keys = ['A', 'B']
    correlation, ax = task_func(data_dict, data_keys)
    assert np.isclose(correlation, -1.0)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_no_correlation():
    data_dict = {
        'A': [1, 2, 3, 4, 5],
        'B': [1, 3, 2, 5, 4]
    }
    data_keys = ['A', 'B']
    correlation, ax = task_func(data_dict, data_keys)
    assert np.isclose(correlation, 0.0, atol=0.5)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_non_numeric_data():
    data_dict = {
        'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']
    }
    data_keys = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)

def test_task_func_with_different_length_data():
    data_dict = {
        'A': [1, 2, 3, 4, 5],
        'B': [1, 2, 3]
    }
    data_keys = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)