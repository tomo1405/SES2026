import matplotlib.pyplot as plt
import numpy as np
from src_0447 import task_func


def test_task_func_default_values():
    X, y, ax = task_func()
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert X.shape == (100, 2)
    assert np.unique(y).size == 3

def test_task_func_custom_values():
    n_samples = 200
    centers = 5
    n_features = 3
    X, y, ax = task_func(n_samples=n_samples, centers=centers, n_features=n_features)
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert X.shape == (n_samples, n_features)
    assert np.unique(y).size == centers

def test_task_func_random_seed():
    X1, y1, _ = task_func(random_seed=42)
    X2, y2, _ = task_func(random_seed=42)
    assert np.array_equal(X1, X2)
    assert np.array_equal(y1, y2)

    X3, y3, _ = task_func(random_seed=99)
    assert not np.array_equal(X1, X3)
    assert not np.array_equal(y1, y3)