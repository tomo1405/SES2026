import pytest
from src_0452 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default():
    X_transformed, ax = task_func()
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, plt.Axes)

def test_task_func_n_components_1():
    X_transformed, ax = task_func(n_components=1)
    assert X_transformed.shape == (500, 1)
    assert ax is None

def test_task_func_custom_dimensions():
    X_transformed, ax = task_func(n_components=3, N_SAMPLES=100, N_FEATURES=20)
    assert X_transformed.shape == (100, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_random_seed():
    X_transformed_1, _ = task_func(random_seed=42)
    X_transformed_2, _ = task_func(random_seed=42)
    assert np.array_equal(X_transformed_1, X_transformed_2)

def test_task_func_no_random_seed():
    X_transformed_1, _ = task_func()
    X_transformed_2, _ = task_func()
    assert not np.array_equal(X_transformed_1, X_transformed_2)