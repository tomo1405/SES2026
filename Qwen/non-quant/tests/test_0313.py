import matplotlib.pyplot as plt
from src_0313 import task_func


def test_task_func_default_bins():
    distribution, ax = task_func()
    assert len(distribution) == 1000
    assert len(ax.patches) == 30

def test_task_func_custom_bins():
    bins = 50
    distribution, ax = task_func(bins=bins)
    assert len(distribution) == 1000
    assert len(ax.patches) == bins

def test_task_func_distribution_values():
    distribution, _ = task_func()
    assert all(isinstance(value, float) for value in distribution)

def test_task_func_ax_type():
    _, ax = task_func()
    assert isinstance(ax, plt.Axes)