import pytest
from src_0447 import task_func

def test_task_func():
    X, y, ax = task_func()
    assert X.shape == (100, 2)
    assert y.shape == (100,)
    assert ax.shape == (100, 2)

def test_task_func_with_custom_params():
    X, y, ax = task_func(n_samples=50, centers=5, n_features=3, random_seed=123)
    assert X.shape == (50, 3)
    assert y.shape == (50,)
    assert ax.shape == (50, 3)

def test_task_func_with_invalid_params():
    with pytest.raises(ValueError):
        task_func(n_samples=-1, centers=3, n_features=2, random_seed=42)

    with pytest.raises(ValueError):
        task_func(n_samples=100, centers=-1, n_features=2, random_seed=42)

    with pytest.raises(ValueError):
        task_func(n_samples=100, centers=3, n_features=-1, random_seed=42)

    with pytest.raises(ValueError):
        task_func(n_samples=100, centers=3, n_features=2, random_seed=-1)