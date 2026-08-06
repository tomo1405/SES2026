import matplotlib.pyplot as plt
import numpy as np
from src_0452 import task_func


def test_task_func():
    # Test with n_components=2
    X_transformed, ax = task_func(n_components=2)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, plt.Axes)

    # Test with n_components=1
    X_transformed, ax = task_func(n_components=1)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 1)
    assert ax is None

    # Test with random_seed
    X_transformed, ax = task_func(random_seed=42)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, plt.Axes)