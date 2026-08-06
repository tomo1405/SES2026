import pytest
from src_0451 import task_func

def test_task_func():
    # Test with default parameters
    cdist, ax = task_func()
    assert cdist.shape == (200, 200)
    assert ax is not None

    # Test with custom parameters
    cdist, ax = task_func(n_samples=300, centers=5, plot_path='test_plot.png')
    assert cdist.shape == (300, 300)
    assert ax is not None
    assert 'test_plot.png' in plt.get_fignums()

    # Test with random seed
    cdist, ax = task_func(random_seed=42)
    assert cdist.shape == (200, 200)
    assert ax is not None

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(n_samples=-1)
    with pytest.raises(ValueError):
        task_func(centers=0)
    with pytest.raises(ValueError):
        task_func(plot_path=None, random_seed=None)