import pytest
from src_0447 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    X, y, ax = task_func()
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert X.shape == (100, 2)
    assert y.shape == (100,)
    assert len(np.unique(y)) == 3

def test_task_func_custom_parameters():
    X, y, ax = task_func(n_samples=200, centers=5, n_features=3, random_seed=99)
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert X.shape == (200, 3)
    assert y.shape == (200,)
    assert len(np.unique(y)) == 5

def test_task_func_random_seed_consistency():
    X1, y1, _ = task_func(random_seed=42)
    X2, y2, _ = task_func(random_seed=42)
    assert np.array_equal(X1, X2)
    assert np.array_equal(y1, y2)

def test_task_func_plot():
    X, y, ax = task_func()
    assert ax.get_xlabel() == 'Feature 1'
    assert ax.get_ylabel() == 'Feature 2'
    assert len(ax.collections) > 0  # There should be at least one scatter plot collection