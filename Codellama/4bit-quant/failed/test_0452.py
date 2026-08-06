import pytest
from src_0452 import task_func

def test_task_func():
    # Test with default values
    X_transformed, ax = task_func()
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test with custom values
    X_transformed, ax = task_func(n_components=3, N_SAMPLES=1000, N_FEATURES=100)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (1000, 3)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test with random seed
    X_transformed, ax = task_func(random_seed=42)
    assert isinstance(X_transformed, np.ndarray)
    assert X_transformed.shape == (500, 2)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(n_components=0)
    with pytest.raises(ValueError):
        task_func(N_SAMPLES=0)
    with pytest.raises(ValueError):
        task_func(N_FEATURES=0)
    with pytest.raises(ValueError):
        task_func(random_seed=-1)