import pytest
from src_0978 import task_func
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func_basic():
    array = np.array([[1, 2], [3, 4]])
    ax = task_func(array)
    assert isinstance(ax, plt.Axes)
    plt.close()

def test_task_func_with_features():
    array = np.array([[1, 2], [3, 4]])
    features = ['a', 'b']
    ax = task_func(array, features=features)
    assert isinstance(ax, plt.Axes)
    plt.close()

def test_task_func_with_seed():
    array = np.array([[1, 2], [3, 4]])
    seed = 42
    ax = task_func(array, seed=seed)
    assert isinstance(ax, plt.Axes)
    plt.close()

def test_task_func_empty_array():
    array = np.array([])
    with pytest.raises(ValueError, match="Input array must be 2-dimensional and non-empty."):
        task_func(array)

def test_task_func_non_2d_array():
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError, match="Input array must be 2-dimensional and non-empty."):
        task_func(array)

def test_task_func_mismatched_features():
    array = np.array([[1, 2], [3, 4]])
    features = ['a']
    with pytest.raises(ValueError, match="Features list must match the number of columns in the array."):
        task_func(array, features=features)

def test_task_func_no_return_value():
    array = np.array([[1, 2], [3, 4]])
    ax = task_func(array)
    assert ax is not None
    plt.close()