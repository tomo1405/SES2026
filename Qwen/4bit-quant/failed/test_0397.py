import pytest
from src_0397 import task_func

def test_task_func_positive_sample_size():
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, sample_size=-1)

def test_task_func_zero_sample_size():
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, sample_size=0)

def test_task_func_valid_input():
    ax = task_func(mu=0, sigma=1, sample_size=100)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_reproducibility():
    ax1 = task_func(mu=0, sigma=1, sample_size=100, seed=42)
    ax2 = task_func(mu=0, sigma=1, sample_size=100, seed=42)
    assert np.array_equal(ax1.lines[0].get_xdata(), ax2.lines[0].get_xdata())
    assert np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())

def test_task_func_different_seed():
    ax1 = task_func(mu=0, sigma=1, sample_size=100, seed=42)
    ax2 = task_func(mu=0, sigma=1, sample_size=100, seed=43)
    assert not np.array_equal(ax1.lines[0].get_xdata(), ax2.lines[0].get_xdata())
    assert not np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())