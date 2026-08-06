import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0978 import task_func


def test_task_func_basic():
    array = np.array([[1, 2], [3, 4]])
    ax = task_func(array)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_features():
    array = np.array([[1, 2], [3, 4]])
    features = ['A', 'B']
    ax = task_func(array, features=features)
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_array():
    array = np.array([])
    with pytest.raises(ValueError):
        task_func(array)

def test_task_func_1d_array():
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(array)

def test_task_func_mismatched_features():
    array = np.array([[1, 2], [3, 4]])
    features = ['A']
    with pytest.raises(ValueError):
        task_func(array, features=features)

def test_task_func_seed():
    array = np.array([[1, 2], [3, 4]])
    seed = 42
    ax1 = task_func(array, seed=seed)
    ax2 = task_func(array, seed=seed)
    assert np.array_equal(ax1.collections[0].get_array().data, ax2.collections[0].get_array().data)

def test_task_func_no_features():
    array = np.array([[1, 2], [3, 4]])
    ax = task_func(array)
    assert ax.get_xticklabels() == ['1', '2']