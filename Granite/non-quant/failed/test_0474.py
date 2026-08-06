import numpy as np
import matplotlib.pyplot as plt
import itertools
from src_0474 import task_func

def test_task_func_valid_input():
    n_walks = 5
    n_steps = 10
    seed = 42
    ax = task_func(n_walks, n_steps, seed)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_input():
    n_walks = -1
    n_steps = -5
    seed = 42
    with pytest.raises(ValueError):
        task_func(n_walks, n_steps, seed)

def test_task_func_default_seed():
    n_walks = 5
    n_steps = 10
    ax1 = task_func(n_walks, n_steps)
    ax2 = task_func(n_walks, n_steps)
    assert not np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())