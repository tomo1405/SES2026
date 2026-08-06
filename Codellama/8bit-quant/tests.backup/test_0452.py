import pytest
from src_0452 import task_func

def test_task_func():
    # Test with default values
    X_transformed, ax = task_func()
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, plt.Axes)

    # Test with n_components=3
    X_transformed, ax = task_func(n_components=3)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 3)
    assert isinstance(ax, plt.Axes)

    # Test with random_seed=42
    X_transformed, ax = task_func(random_seed=42)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, plt.Axes)

    # Test with N_SAMPLES=1000
    X_transformed, ax = task_func(N_SAMPLES=1000)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (1000, 2)
    assert isinstance(ax, plt.Axes)

    # Test with N_FEATURES=100
    X_transformed, ax = task_func(N_FEATURES=100)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, plt.Axes)