python
import pytest
from src_0397 import task_func

def test_task_func():
    # Test case 1: sample_size is a positive integer
    mu = 0
    sigma = 1
    sample_size = 100
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Gaussian KDE'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'Density'
    assert len(ax.lines) == 1
    assert ax.lines[0].get_color() == 'black'
    assert ax.lines[0].get_label() == 'KDE'
    assert len(ax.patches) == 0
    
    # Test case 2: sample_size is zero
    mu = 0
    sigma = 1
    sample_size = 0
    seed = 0
    with pytest.raises(ValueError):
        ax = task_func(mu, sigma, sample_size, seed)