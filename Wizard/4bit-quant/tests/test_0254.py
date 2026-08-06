python
import numpy as np
import random
import pytest

# Constants
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def task_func(ax):

    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(random.randint(1, 10)*x)

    color = random.choice(COLORS)
    ax.plot(x, y, color=color)
    ax.set_rlabel_position(random.randint(0, 180))

    return color

def test_task_func():
    fig, ax = plt.subplots()
    color = task_func(ax)
    assert color in COLORS