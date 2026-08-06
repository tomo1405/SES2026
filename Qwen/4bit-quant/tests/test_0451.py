import os

import matplotlib.pyplot as plt
import numpy as np
from src_0451 import task_func


def test_task_func_default():
    distances, ax = task_func()
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (200, 200)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_plot_path(tmpdir):
    plot_path = str(tmpdir.join('test_plot.png'))
    distances, ax = task_func(plot_path=plot_path)
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (200, 200)
    assert ax is None
    assert os.path.exists(plot_path)

def test_task_func_random_seed():
    distances1, _ = task_func(random_seed=42)
    distances2, _ = task_func(random_seed=42)
    assert np.array_equal(distances1, distances2)

def test_task_func_custom_parameters():
    distances, ax = task_func(n_samples=100, centers=3)
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (100, 100)
    assert isinstance(ax, plt.Axes)