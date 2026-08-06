import pytest
from src_0452 import task_func
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func_default():
    X_transformed, ax = task_func()
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, plt.Axes)

def test_task_func_one_component():
    X_transformed, ax = task_func(n_components=1)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 1)
    assert ax is None

def test_task_func_custom_dimensions():
    X_transformed, ax = task_func(n_components=3, N_SAMPLES=1000, N_FEATURES=20)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (1000, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_random_seed():
    X_transformed_1, _ = task_func(random_seed=42)
    X_transformed_2, _ = task_func(random_seed=42)
    assert np.array_equal(X_transformed_1, X_transformed_2)

def test_task_func_no_random_seed():
    X_transformed_1, _ = task_func()
    X_transformed_2, _ = task_func()
    assert not np.array_equal(X_transformed_1, X_transformed_2)

def test_task_func_invalid_n_components():
    with pytest.raises(ValueError):
        task_func(n_components=0)

def test_task_func_invalid_N_SAMPLES():
    with pytest.raises(ValueError):
        task_func(N_SAMPLES=-1)

def test_task_func_invalid_N_FEATURES():
    with pytest.raises(ValueError):
        task_func(N_FEATURES=-1)