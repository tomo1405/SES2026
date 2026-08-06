import matplotlib.pyplot as plt
import numpy as np
from src_0447 import task_func


def test_task_func_default_parameters():
    X, y, ax = task_func()
    assert X.shape == (100, 2)
    assert len(np.unique(y)) == 3
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_parameters():
    X, y, ax = task_func(n_samples=200, centers=4, n_features=3, random_seed=123)
    assert X.shape == (200, 3)
    assert len(np.unique(y)) == 4
    assert isinstance(ax, plt.Axes)

def test_task_func_random_seed_consistency():
    X1, y1, _ = task_func(random_seed=42)
    X2, y2, _ = task_func(random_seed=42)
    assert np.array_equal(X1, X2)
    assert np.array_equal(y1, y2)

def test_task_func_random_seed_inconsistency():
    X1, y1, _ = task_func(random_seed=42)
    X2, y2, _ = task_func(random_seed=56)
    assert not np.array_equal(X1, X2)
    assert not np.array_equal(y1, y2)