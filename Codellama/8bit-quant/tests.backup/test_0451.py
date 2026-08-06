import pytest
from src_0451 import task_func

def test_task_func():
    # Test with default parameters
    cdist, ax = task_func()
    assert cdist.shape == (200, 200)
    assert ax is not None

    # Test with custom parameters
    cdist, ax = task_func(n_samples=300, centers=5, plot_path='test.png', random_seed=42)
    assert cdist.shape == (300, 300)
    assert ax is not None

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(n_samples=-1, centers=4, plot_path='test.png', random_seed=42)

    with pytest.raises(ValueError):
        task_func(n_samples=300, centers=-1, plot_path='test.png', random_seed=42)

    with pytest.raises(ValueError):
        task_func(n_samples=300, centers=4, plot_path=None, random_seed=42)

    with pytest.raises(ValueError):
        task_func(n_samples=300, centers=4, plot_path='test.png', random_seed=-1)