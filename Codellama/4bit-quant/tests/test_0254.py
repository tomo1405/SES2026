import random

import numpy as np
from src_0254 import task_func


def test_task_func():
    ax = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(random.randint(1, 10)*x)
    color = random.choice(COLORS)
    ax.plot(x, y, color=color)
    ax.set_rlabel_position(random.randint(0, 180))
    assert task_func(ax) == color