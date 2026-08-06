python
import pytest
from src_0451 import task_func

def test_task_func():
    # Test default values
    result = task_func()
    assert len(result) == 2
    assert isinstance(result[0], numpy.ndarray)
    assert result[0].shape == (200, 200)
    assert result[1] is None

    # Test with n_samples=100, centers=2, plot_path='test.png'
    result = task_func(n_samples=100, centers=2, plot_path='test.png')
    assert len(result) == 2
    assert isinstance(result[0], numpy.ndarray)
    assert result[0].shape == (100, 100)
    assert isinstance(result[1], matplotlib.axes.Axes)

    # Test with random_seed=42
    result = task_func(random_seed=42)
    assert len(result) == 2
    assert isinstance(result[0], numpy.ndarray)
    assert result[0].shape == (200, 200)
    assert result[1] is None