import pytest
from src_0451 import task_func
import numpy as np
import os

@pytest.mark.parametrize("n_samples, centers", [
    (200, 4),
    (100, 3),
    (300, 5)
])
def test_task_func_return_values(n_samples, centers):
    distances, ax_or_none = task_func(n_samples=n_samples, centers=centers)
    
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (n_samples, n_samples)
    
    if ax_or_none is not None:
        assert isinstance(ax_or_none, plt.Axes)
    else:
        assert ax_or_none is None

@pytest.mark.parametrize("plot_path", [
    "test_plot.png",
    "temp/test_plot.png"
])
def test_task_func_with_plot_path(tmpdir, plot_path):
    plot_path = str(tmpdir.join(plot_path))
    distances, ax_or_none = task_func(plot_path=plot_path)
    
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (200, 200)
    assert ax_or_none is None
    
    assert os.path.exists(plot_path)

def test_task_func_random_seed():
    distances1, _ = task_func(random_seed=42)
    distances2, _ = task_func(random_seed=42)
    
    assert np.array_equal(distances1, distances2)

def test_task_func_no_random_seed():
    distances1, _ = task_func()
    distances2, _ = task_func()
    
    assert not np.array_equal(distances1, distances2)