python
import numpy as np
import matplotlib.pyplot as plt
import pytest

# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

def task_func(data_size):
    np.random.seed(0)
    data = np.random.randn(data_size)
    color = np.random.choice(BAR_COLOR)
    plt.hist(data, bins=np.arange(-3, 4, 0.5), color=color, edgecolor='black')
    return data, color

def test_task_func():
    data, color = task_func(100)
    assert len(data) == 100
    assert color in BAR_COLOR