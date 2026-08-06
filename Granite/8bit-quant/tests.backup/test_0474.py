import numpy as np
import matplotlib.pyplot as plt
import itertools
import pytest
from src_0474 import task_func

def test_task_func_valid_input():
    ax = task_func(n_walks=2, n_steps=100)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(n_walks=-1, n_steps=100)
    with pytest.raises(ValueError):
        task_func(n_walks=2, n_steps=-100)

def test_task_func_seed():
    ax1 = task_func(n_walks=2, n_steps=100, seed=42)
    ax2 = task_func(n_walks=2, n_steps=100, seed=42)
    assert np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())
    assert np.array_equal(ax1.lines[1].get_ydata(), ax2.lines[1].get_ydata())

def test_task_func_num_walks():
    ax1 = task_func(n_walks=1, n_steps=100)
    ax2 = task_func(n_walks=2, n_steps=100)
    assert len(ax1.lines) == 1
    assert len(ax2.lines) == 2