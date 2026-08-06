import pytest
from src_0451 import task_func
import numpy as np
import os

def test_task_func_default():
    distances, ax = task_func()
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (200, 200)
    assert ax is not None

def test_task_func_custom_params():
    distances, ax = task_func(n_samples=150, centers=3, random_seed=42)
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (150, 150)
    assert ax is not None

def test_task_func_save_plot(tmpdir):
    plot_path = str(tmpdir / "test_plot.png")
    distances, ax = task_func(plot_path=plot_path)
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (200, 200)
    assert ax is None
    assert os.path.exists(plot_path)

def test_task_func_no_plot():
    distances, ax = task_func(plot_path=None)
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (200, 200)
    assert ax is not None